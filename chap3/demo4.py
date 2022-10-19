import openpyxl
workbook = openpyxl.load_workbook('京东鞋子评论信息.xlsx')
sheet = workbook['评论信息']
rows  = sheet.rows
for row in rows:
    # print(row)
    for cell in row:
        print(cell.value)
        print('++++')