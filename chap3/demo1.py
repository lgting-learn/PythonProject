import openpyxl

workbook = openpyxl.load_workbook('京东鞋子评论信息.xlsx')
print(workbook.sheetnames)

sheet = workbook['评论信息']
print(sheet.dimensions)

cell = sheet['A1']
# print(cell.value)

cells = sheet['A1:D191']
print('cells', cells)
for cell in cells:
    print(cell[0].value)
    print('--------------')
# print(cells)
