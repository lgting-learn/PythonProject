# 教育机构 ：马士兵教育
# 讲    师：杨淑娟

import openpyxl

workbook = openpyxl.load_workbook('京东鞋子评论信息.xlsx')  # 打开工作薄
sheet = workbook['评论信息']  # 获取指定的工作表
cols = sheet['A']
#打印A列所有单元格
for cell in cols:
    print(cell.value)
    print('-------------------------')
# print(cols)
