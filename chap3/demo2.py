import openpyxl
workbook = openpyxl.load_workbook('京东鞋子评论信息.xlsx')
sheet=workbook['评论信息']
cols = sheet['A']
for cell in cols:
    print(cell.value)
    print('+++++++++++++++')
