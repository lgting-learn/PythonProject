# 教育机构 ：马士兵教育
# 讲    师：杨淑娟

import openpyxl
from openpyxl.styles import Alignment

workbook = openpyxl.load_workbook('新表.xlsx')
sheet = workbook['Sheet1']
# A1单元格对齐方式
cell = sheet['A1']
algin = Alignment(horizontal='center', vertical='center')
cell.alignment = algin
workbook.save('新表.xlsx')
