模型是程序生成的
程序我用随机数测试过了，只要数据准确就能跑出准确的模型
给我的箱子尺寸数据是缺的，实际上我只拿到了3个盒子的数据
缺失的数据我不清楚在谁那里，但是建模程序已经写好了，缺失数据请通过编辑box_data文件补全数据用程序把模型自己跑出来（几秒钟的事），跑一百个都没问题。

以下是文档说明：
box_data.csv - 这个文件很重要，程序是根据这个跑的。excel可以打开。里面有我已经得到的3条数据，其余我手上没有，请自行补全。
box_data.xls - 给了一个xls的备份文件，我的建议是打开xls文件在excel里面填入数据（里面怎么填很明确），另存csv文件/当然也可以直接编辑csv
box_generator.py - 主程序，不要乱改
box_generator_data.py - 数据处理程序，不要乱改
STUPID_WORKSHOP.3dm - 空rhino，用来跑程序
STUPID_BOX_SAMPLE1.3dm,STUPID_BOX_SAMPLE2.3dm，STUPID_BOX_SAMPLE3.3dm  - 跑的样例（可以出图用）

以下是使用说明：
步骤0：解压压缩包workshop_modeling，得到文件夹
步骤1：打开box_data.xls，根据标题栏补全里面的数据，注意不要动NUM一列，那个是程序要识别的序号
步骤2：excel另存为box_data.csv文件（注意源文件备份）
步骤3：打开STUPID_BOX.3dm(是个空文件)，工具栏里面Tools-Pythonscript-Edit(工具-PythonScript-编辑)
       注：不同版本rhino可能会有不同叫法，什么python，python指令码，ipython，反正关键字'python'
步骤4：弹出的编程窗口里，File-Open，打开workshop_modeling文件夹下box_generator.py文件
步骤5：编程窗口Tools-reset script engine, 然后debug-start debuging
	(或者通过上面有个绿色三角形下拉菜单里面有个按钮reset engine and debug，效果一样）
步骤6：回到rhino界面，命令行会提示“'choose the box number(NUM value in box_data.csv):'”
	这个时候输入你补上的csv数据前面的标号（也就是NUM一栏的数字，注意不是excel本身的行号！！）
步骤7：回车键，箱子会神奇的自己蹦出来。另存为rhino

注意：
1. 补全数据的时候，要按照‘长-高’‘宽-高’‘长-宽’的顺序填写，具体看我的数据样例
2. 源码禁止外传，上传，分享


