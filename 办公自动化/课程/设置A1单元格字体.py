#教育机构 ：马士兵教育
#讲    师：杨淑娟

import  openpyxl
from  openpyxl.styles import Font
workbook=openpyxl.load_workbook('新表.xlsx')
sheet=workbook['Sheet1']
#设置A1单元格字体
cell=sheet['A1']
font=Font(name='微软雅黑',size=20,bold=True,italic=True,color='ff0000')
cell.font=font
workbook.save('新表.xlsx')
