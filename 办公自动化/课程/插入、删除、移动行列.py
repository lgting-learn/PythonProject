#教育机构 ：马士兵教育
#讲    师：杨淑娟

import  openpyxl
workbook=openpyxl.load_workbook('新表.xlsx')
sheet=workbook['Sheet1']
#sheet.insert_cols(idx=1)
#从第2列开始插入3列
sheet.insert_cols(idx=2,amount=3)
#sheet.insert_rows(idx=2)
#从第4行开始插入3列
sheet.insert_rows(idx=4,amount=3)
#sheet.delete_cols(idx=1,amount=4)
#sheet.delete_rows(idx=2,amount=6)
# 把A2:B6范围内的单元格上移一行，右移两列,将覆盖现有的单元格
# sheet.move_range('A2:B6',rows=-1,cols=2)

workbook.save('新表.xlsx')
