#教育机构 ：马士兵教育
#讲    师：杨淑娟

import  openpyxl
workbook=openpyxl.load_workbook('京东鞋子评论信息.xlsx')  #打开工作薄
sheet=workbook['评论信息']  #获取指定的工作表
#获取x-y行,a-b列范围单元格,按列输出
rows=sheet.iter_cols(min_row=1,max_row=5,min_col=1,max_col=4)
for row in rows:
    for cell in row:
        print(cell.value)
    print('----------------------------------------')
#print(cols)