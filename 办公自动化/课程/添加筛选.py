#教育机构 ：马士兵教育
#讲    师：杨淑娟

import openpyxl
workbook=openpyxl.load_workbook('京东鞋子评论信息.xlsx')

sheet=workbook['mysheet']
#添加筛选
sheet.auto_filter.ref=sheet.dimensions
workbook.save('京东鞋子评论信息.xlsx')