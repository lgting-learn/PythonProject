import openpyxl
workbook = openpyxl.load_workbook('京东鞋子评论信息.xlsx')
sheet = workbook['评论信息']
# 将41码所在的行复制到另一个新的表格
rows = sheet.rows#获取sheet表所有行
new_lst = []
for row in rows:
    if row[3].value == '41' or row[3].value == '鞋码':
        sub_lst = []
        for i in range(0, 4):
            sub_lst.append(row[i].value)
        new_lst.append(sub_lst)
print(new_lst)
# 创建新的工作簿
workbookNew = openpyxl.Workbook()
sheetNew = workbookNew.active
for row in new_lst:
    sheetNew.append(row)  # 复制行
workbookNew.save("41码数1.xlsx")
