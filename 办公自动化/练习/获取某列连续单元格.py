import openpyxl
#加载表格
workbook = openpyxl.load_workbook('京东鞋子评论信息.xlsx')
# print(workbook.sheetnames)
#获取指定工作簿
sheet = workbook['评论信息']
#打印工作簿规模
# print(sheet.dimensions)
#获取单元格
cell = sheet['A1']
# print(cell.value)
#获取连续单元格,打印A1-A5单元格内容
cells = sheet['A1:A5']
for cell in cells:
    print(cell[0].value)
    print('-'*10)