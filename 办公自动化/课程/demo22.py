#教育机构 ：马士兵教育
#讲    师：杨淑娟

import  openpyxl
from  openpyxl.styles import Side,Border
workbook=openpyxl.load_workbook('新表.xlsx')
sheet=workbook['Sheet1']
cell=sheet['A1']
side=Side(style='thin',color='ff0000')  #设置线条的形状与颜色
border=Border(left=side,top=side,right=side,bottom=side)
cell.border=border
workbook.save('新表.xlsx')

