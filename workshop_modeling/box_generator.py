# -*# -*- coding: utf-8 -*-

##############################
# code by : Zhengyang Chen   #
# 15 Feb 2018                #
# Ver 1.10                   #
##############################

#statement---------------------->
# This code is for stupid workshop'
# The workshop is a waste of time while coding isn't

#prerequisites------------------->
# path operation required - same folder
# csv file required
# rhinoceros sr9 or newer 64bits required
# rhino iPython standard lib required


# headers---------------------->
import rhinoscriptsyntax as rs
import scriptcontext as sc
import box_generator_data as bd
#import csv    ---- N/A in rhino python

OK=0
ERROR=-1
TRUE=1
FALSE=0
OVERFLOW=-2

#globals----------------->
ZERO=[0,0,0]
cut1=2
cut2=0.5
cut3=3
cut4=3

# box operation---------------------->
class box:
    def __init__(self):
        self.tag=-1 #-1- NaB, 0-out , 1- in
        self.data=None
        self.geo=None
        self.height=None
    def console(self,data,tag,gap):
        self.tag=tag
        self.data=data
        self.height=data[1]
        #print self.data
        if tag==0:self.geo=self.outbox(gap)
        elif tag==1:self.geo=self.inbox(gap)
        return self.geo
        
    def outbox(self,gap):
        #DEFINE BASE SLICE------------>
        rec_lr=rs.AddRectangle(rs.WorldYZPlane(),self.data[0],self.data[1])
        srf_lr=rs.AddPlanarSrf(rec_lr)
        rec_lr=rs.MoveObject(rec_lr,rs.VectorCreate(ZERO,rs.SurfaceAreaCentroid(srf_lr)[0]))
        rs.DeleteObject(srf_lr)
        rec_lr=cutrec(2,rec_lr,gap)
        srf_lr=rs.AddPlanarSrf(rec_lr)
        rs.DeleteObjects(rec_lr)
        ### CANNOT USE WORLDZX()---------->
        xz=rs.PlaneFromFrame([0,0,0],[1,0,0],[0,0,1])
        rec_fk=rs.AddRectangle(xz,self.data[2],self.data[3])
        ###<-------------
        srf_fk=rs.AddPlanarSrf(rec_fk)
        rec_fk=rs.MoveObject(rec_fk,rs.VectorCreate(ZERO,rs.SurfaceAreaCentroid(srf_fk)[0]))
        rs.DeleteObject(srf_fk)
        rec_fk=cutrec(2,rec_fk,gap)
        srf_fk=rs.AddPlanarSrf(rec_fk)
        rs.DeleteObjects(rec_fk)
        rec_tb=rs.AddRectangle(rs.WorldXYPlane(),self.data[5],self.data[4])
        srf_tb=rs.AddPlanarSrf(rec_tb)
        rec_tb=rs.MoveObject(rec_tb,rs.VectorCreate(ZERO,rs.SurfaceAreaCentroid(srf_tb)[0]))
        rs.DeleteObject(srf_tb)
        rec_tb=cutrec(1,rec_tb,0)
        srf_tb=rs.AddPlanarSrf(rec_tb)
        rs.DeleteObject(rec_tb)
        
        #CONSTRUCT THE BOX-------------------->
        srfs=[]
        srfs.append(rs.CopyObject(srf_tb,[0,0,self.data[3]/2.0]))
        srfs.append(rs.CopyObject(srf_tb,[0,0,self.data[3]/(-2.0)]))
        srfs.append(rs.CopyObject(srf_fk,[0,self.data[0]/2.0,0]))
        srfs.append(rs.MirrorObject(rs.CopyObject(srf_fk,[0,self.data[0]/(-2.0),0]),[0,1,0],[0,0,1]))
        srfs.append(rs.CopyObject(srf_lr,[self.data[5]/(-2.0),0,0]))
        srfs.append(rs.MirrorObject(rs.CopyObject(srf_lr,[self.data[5]/(2.0),0,0]),[1,0,0],[0,0,1]))
        
        bele=[]
        for srf in srfs:
            extvec=rs.VectorCreate(ZERO, rs.SurfaceAreaCentroid(srf)[0])
            max,sign,loc=0,-1,0
            for i in range(len(extvec)):
                if abs(extvec[i])>max:
                    max=abs(extvec[i])
                    sign=extvec[i]
                    loc=i
            if loc==0:
                line=rs.AddLine(ZERO,rs.VectorScale(rs.VectorUnitize([sign,0,0]),cut2))
                bele.append(rs.ExtrudeSurface(srf,line))
            elif loc==1:
                line=rs.AddLine(ZERO,rs.VectorScale(rs.VectorUnitize([0,sign,0]),cut2))
                bele.append(rs.ExtrudeSurface(srf,line))
            elif loc==2:
                line=rs.AddLine(ZERO,rs.VectorScale(rs.VectorUnitize([0,0,sign]),cut2))
                bele.append(rs.ExtrudeSurface(srf,line))
            rs.DeleteObject(line)
        rs.DeleteObjects(srfs)
        rs.DeleteObjects([srf_lr,srf_fk,srf_tb])
        return bele
        
    def inbox(self,gap):
        #DEFINE BASE SLICE------------>
        rec_lr=rs.AddRectangle(rs.WorldYZPlane(),self.data[0],self.data[1])
        srf_lr=rs.AddPlanarSrf(rec_lr)
        rec_lr=rs.MoveObject(rec_lr,rs.VectorCreate(ZERO,rs.SurfaceAreaCentroid(srf_lr)[0]))
        rs.DeleteObject(srf_lr)
        rec_lr=cutrec(3,rec_lr,gap)
        srf_lr=rs.AddPlanarSrf(rec_lr)
        rs.DeleteObjects(rec_lr)
        ### CANNOT USE WORLDZX()---------->
        xz=rs.PlaneFromFrame([0,0,0],[1,0,0],[0,0,1])
        rec_fk=rs.AddRectangle(xz,self.data[2],self.data[3])
        ###<-------------
        srf_fk=rs.AddPlanarSrf(rec_fk)
        rec_fk=rs.MoveObject(rec_fk,rs.VectorCreate(ZERO,rs.SurfaceAreaCentroid(srf_fk)[0]))
        rs.DeleteObject(srf_fk)
        rec_fk=cutrec(3,rec_fk,gap)
        srf_fk=rs.AddPlanarSrf(rec_fk)
        rs.DeleteObjects(rec_fk)
        rec_tb=rs.AddRectangle(rs.WorldXYPlane(),self.data[5],self.data[4])
        srf_tb=rs.AddPlanarSrf(rec_tb)
        rec_tb=rs.MoveObject(rec_tb,rs.VectorCreate(ZERO,rs.SurfaceAreaCentroid(srf_tb)[0]))
        rs.DeleteObject(srf_tb)
        rec_tb=cutrec(1,rec_tb,0)
        srf_tb=rs.AddPlanarSrf(rec_tb)
        rs.DeleteObject(rec_tb)
        
        #CONSTRUCT THE BOX-------------------->
        srfs=[]
        
        srfs.append(rs.CopyObject(srf_tb,[0,0,self.data[3]/2.0-gap]))
        srfs.append(rs.CopyObject(srf_tb,[0,0,self.data[3]/(-2.0)]))
        srfs.append(rs.CopyObject(srf_fk,[0,self.data[4]/2.0,0]))
        srfs.append(rs.MirrorObject(rs.CopyObject(srf_fk,[0,self.data[4]/(-2.0),0]),[0,1,0],[0,0,1]))
        srfs.append(rs.CopyObject(srf_lr,[self.data[5]/(-2.0),0,0]))
        srfs.append(rs.MirrorObject(rs.CopyObject(srf_lr,[self.data[5]/(2.0),0,0]),[1,0,0],[0,0,1]))
        bele=[]
        for srf in srfs:
            extvec=rs.VectorCreate(ZERO, rs.SurfaceAreaCentroid(srf)[0])
            max,sign,loc=0,-1,0
            for i in range(len(extvec)):
                if abs(extvec[i])>max:
                    max=abs(extvec[i])
                    sign=extvec[i]
                    loc=i
            if loc==0:
                line=rs.AddLine(ZERO,rs.VectorScale(rs.VectorUnitize([sign,0,0]),cut2))
                bele.append(rs.ExtrudeSurface(srf,line))
            elif loc==1:
                line=rs.AddLine(ZERO,rs.VectorScale(rs.VectorUnitize([0,sign,0]),cut2))
                bele.append(rs.ExtrudeSurface(srf,line))
            elif loc==2:
                line=rs.AddLine(ZERO,rs.VectorScale(rs.VectorUnitize([0,0,sign]),cut2))
                bele.append(rs.ExtrudeSurface(srf,line))
            rs.DeleteObject(line)
        rs.DeleteObjects(srfs)
        rs.DeleteObjects([srf_lr,srf_fk,srf_tb])
        return bele

def cutrec(type,rec,gap):
    
    if type==1:
        #out-tbcut
        pts=rs.CurvePoints(rec)
        newpts=[]
        for i in range(len(pts)-1):
            m,n=i-1,i+1
            if m<0:m=3
            if n>3:n=0
            basevec_x=rs.VectorUnitize(rs.VectorCreate(pts[m],pts[i]))
            basevec_y=rs.VectorUnitize(rs.VectorCreate(pts[n],pts[i]))
            #print basevec_x,basevec_y
            newpts.append(rs.PointAdd(pts[i],rs.VectorScale(basevec_x,cut1)))
            newpts.append(rs.PointAdd(pts[i],rs.VectorAdd(rs.VectorScale(basevec_x,cut1),rs.VectorScale(basevec_y,cut2))))
            newpts.append(rs.PointAdd(pts[i],rs.VectorAdd(rs.VectorScale(basevec_x,cut2),rs.VectorScale(basevec_y,cut2))))
            newpts.append(rs.PointAdd(pts[i],rs.VectorAdd(rs.VectorScale(basevec_x,cut2),rs.VectorScale(basevec_y,cut1))))
            newpts.append(rs.PointAdd(pts[i],rs.VectorScale(basevec_y,cut1)))
        newpts.append(newpts[0])
        #---->add startpoint to make sure close curve
        poly=rs.AddPolyline(newpts)
        rs.DeleteObject(rec)
        return poly
        
    elif type==2:
        #out-sidecut
        pts=rs.CurvePoints(rec)
        newpts=[]
        for i in range(len(pts)-1):
            m,n=i-1,i+1
            if m<0:m=3
            if n>3:n=0
            basevec_x=rs.VectorUnitize(rs.VectorCreate(pts[m],pts[i]))
            basevec_y=rs.VectorUnitize(rs.VectorCreate(pts[n],pts[i]))
            #print basevec_x,basevec_y
            pt1=(rs.PointAdd(pts[i],rs.VectorScale(basevec_x,cut1)))
            pt2=(rs.PointAdd(pts[i],rs.VectorAdd(rs.VectorScale(basevec_x,cut1),rs.VectorScale(basevec_y,cut2))))
            pt3=(rs.PointAdd(pts[i],rs.VectorAdd(rs.VectorScale(basevec_x,cut2),rs.VectorScale(basevec_y,cut1))))
            pt4=(rs.PointAdd(pts[i],rs.VectorScale(basevec_y,cut1)))
            pt5=(rs.PointAdd(pts[i],rs.VectorScale(basevec_y,cut2)))
            pt6=(rs.PointAdd(pts[i],rs.VectorScale(basevec_x,cut2)))
            if i==0:newpts.extend([pt1,pt2,pt5,pt4,pt3])
            elif i==3: newpts.extend([pt2,pt1,pt6,pt3,pt4])
            else:newpts.extend([pt2,pt1,pts[i],pt4,pt3])
        newpts.append(newpts[0])
        #---->add startpoint to make sure close curve
        poly=rs.AddPolyline(newpts)
        rs.DeleteObject(rec)
        return poly
        
    elif type==3:
        #IN-CUT
        pts=rs.CurvePoints(rec)
        newpts=[]
        for i in range(len(pts)-1):
            m,n=i-1,i+1
            if m<0:m=3
            if n>3:n=0
            basevec_x=rs.VectorUnitize(rs.VectorCreate(pts[m],pts[i]))
            basevec_y=rs.VectorUnitize(rs.VectorCreate(pts[n],pts[i]))
            #print basevec_x,basevec_y
            pt1=(rs.PointAdd(pts[i],rs.VectorScale(basevec_x,cut4)))
            pt2=(rs.PointAdd(pts[i],rs.VectorScale(basevec_y,cut4)))
            pt3=(rs.PointAdd(pts[i],rs.VectorAdd(rs.VectorScale(basevec_x,cut4),rs.VectorScale(basevec_y,cut2+gap))))
            pt4=(rs.PointAdd(pts[i],rs.VectorAdd(rs.VectorScale(basevec_x,cut2+gap),rs.VectorScale(basevec_y,cut4))))
            pt5=(rs.PointAdd(pts[i],rs.VectorScale(basevec_x,cut2+gap)))
            pt6=(rs.PointAdd(pts[i],rs.VectorScale(basevec_y,cut2+gap)))
            pt7=(rs.PointAdd(pts[i],rs.VectorScale(basevec_x,gap+cut1)))
            pt8=(rs.PointAdd(pts[i],rs.VectorScale(basevec_y,gap+cut1)))
            pt9=(rs.PointAdd(pts[i],rs.VectorAdd(rs.VectorScale(basevec_x,gap+cut1),rs.VectorScale(basevec_y,cut2+gap))))
            ptx=(rs.PointAdd(pts[i],rs.VectorAdd(rs.VectorScale(basevec_x,cut2+gap),rs.VectorScale(basevec_y,gap+cut1))))
            ptx1=(rs.PointAdd(pts[i],rs.VectorAdd(rs.VectorScale(basevec_x,gap+cut1),rs.VectorScale(basevec_y,cut2))))
            ptx2=(rs.PointAdd(pts[i],rs.VectorAdd(rs.VectorScale(basevec_x,cut2),rs.VectorScale(basevec_y,gap+cut1))))
            if i==0:newpts.extend([pt3,pt1,pts[i],pt8,ptx2])
            elif i==1: newpts.extend([ptx1,pt7,pt5,pt4,pt2])
            elif i==2: newpts.extend([pt1,pt3,pt6,pt8,ptx])
            else:newpts.extend([pt9,pt7,pts[i],pt2,pt4])
            
        newpts.append(newpts[0])
        #---->add startpoint to make sure close curve
        poly=rs.AddPolyline(newpts)
        rs.DeleteObject(rec)
        return poly
    

class device:
    def __init__(self):
        self.id=None
        self.data=None
        self.geo=[]
        self.opt=[0,0,0]
    def console(self,boxnum):
        self.id=boxnum
        self.data=bd.read_data(boxnum)
        self.place_box()
    def place_box(self):
        myBox1=box()
        box1=myBox1.console(self.data[2],0,0)
        myBox2=box()
        box2=myBox2.console(self.data[1],1,(self.data[1][0]-self.data[0][0]-2*cut2)/2.0)
        myBox3=box()
        box3=myBox3.console(self.data[0],1,(self.data[1][0]-self.data[0][0]-2*cut2)/2.0)
        rs.MoveObjects(box1,(0,0,myBox1.height/2.0))
        rs.MoveObjects(box2,(0,0,myBox2.height/2.0+cut2))
        rs.MoveObjects(box3,(0,0,myBox3.height/2.0+2*cut2))

if __name__=='__main__':
    myDev=device()
    num=rs.GetInteger('choose the box number(NUM value in box_data.csv):',4,1,40)
    myDev.console(num)
