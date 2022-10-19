import openpyxl

workbook = openpyxl.load_workbook('京东鞋子评论信息.xlsx')
sheet=workbook['评论信息']
cols=sheet['A:C']
for col in cols:
    for cell in col:
        print('cell',cell.value)
        print('++')