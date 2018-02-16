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
#import csv    ---- N/A in rhino python

OK=0
ERROR=-1
TRUE=1
FALSE=0
OVERFLOW=-2

# readfile---------------------->

def data_processing():
    with open('box_data.csv','rb') as myFile:
        lines=myFile.readlines()
        if not lines:
            rs.MessageBox('EMPTY FILE!')
            return ERROR
        dataset=[]
        dataline=[]
        for line in lines:
            line=line.strip()
            line=line.split(',')
            #print line
            dataset.append(line)
        #print dataset[4][3]
        return dataset
        
def read_data(line):
    dataset=data_processing()
    if line==0 or line+1>len(dataset):
        rs.MessageBox('DATA OVERFLOW!')
        return OVERFLOW 
    if dataset[line][1]=='-1':
        rs.MessageBox('INVALID DATA:NO INPUT!')
        return ERROR
        
    boxdata=[[],[],[],line]
    for i in range(1,len(dataset[line])):
        if i<=6: boxdata[0].append(float(dataset[line][i]))
        elif i<=12: boxdata[1].append(float(dataset[line][i]))
        elif dataset[line][i]:boxdata[2].append(float(dataset[line][i]))
    #print boxdata
    return boxdata

"""

if __name__=='__main__':
    ds=data_processing()
    read_data(1,ds)

"""