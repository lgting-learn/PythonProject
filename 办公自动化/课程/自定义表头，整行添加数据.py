#教育机构 ：马士兵教育
#讲    师：杨淑娟

import  openpyxl
workbook=openpyxl.load_workbook('新表.xlsx')

sheet=workbook['Sheet1']
#自定义表头，整行添加数据
lst=['姓名','分数']
sheet.append(lst)

stu_lst=[
    ['张三',90],
    ['李四',98],
    ['王五',100],
    ['陈六',70]
]
#整行数据添加
for row in stu_lst:
    sheet.append(row)
workbook.save('新表.xlsx')