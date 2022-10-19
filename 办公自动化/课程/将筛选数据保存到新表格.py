# 教育机构 ：马士兵教育
# 讲    师：杨淑娟

import openpyxl

workbook = openpyxl.load_workbook('京东鞋子评论信息.xlsx')
sheet = workbook['mysheet']
# 将筛选数据保存到新表格
# 获取所有行
rows = sheet.rows
lst = []
for row in rows:
    # print(row)
    if row[3].value == '41':
        sub_lst = []
        for i in range(0, 4):
            sub_lst.append(row[i].value)
        lst.append(sub_lst)

# 存放到一个新的Excel文件中
new_workbook = openpyxl.Workbook()
new_sheet = new_workbook.active
for row in lst:
    new_sheet.append(row)

new_workbook.save('41码鞋子评论数据.xlsx')
