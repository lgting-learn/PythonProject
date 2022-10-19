#教育机构 ：马士兵教育
#讲    师：杨淑娟

import  openpyxl
workbook=openpyxl.load_workbook('新表.xlsx')

sheet=workbook['Sheet1']
#计算总分和
sheet['B9']='=sum(B5:B8)'
workbook.save('新表.xlsx')