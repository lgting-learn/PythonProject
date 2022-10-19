#教育机构 ：马士兵教育
#讲    师：杨淑娟

import  openpyxl
workbook=openpyxl.load_workbook('京东鞋子评论信息.xlsx')  #打开工作薄
sheet=workbook['评论信息']  #获取指定的工作表
#获取工作簿所有列 逐列打印单元格
cols=sheet.columns
for col in cols:
    for cell in col:
        print(cell.value)
    print('------------------------------')
print(cols)
#print(cols)