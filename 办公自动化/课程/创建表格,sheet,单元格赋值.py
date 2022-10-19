#教育机构 ：马士兵教育
#讲    师：杨淑娟

import  openpyxl
workbook=openpyxl.Workbook()  #创建一个新的工作薄，Excel文件
#创建名为test的工作簿
sheet=workbook.create_sheet('test')
#设置A1单元格的值
sheet['A1']='hello,Python'
workbook.save('新表11.xlsx')