import openpyxl  # 引入模块
workbook = openpyxl.load_workbook('京东鞋子评论信息.xlsx')  # 加载工作簿
sheet = workbook['评论信息']  # 获取工作表
cell = sheet['A1']  # 获取A1单元格
cellVal = cell.value  # 获取A1单元格的值
cells = sheet['A']  # 获取A列全部单元格
cells = sheet['A1:A5']  # 获取A1-A5行的全部单元格
cells = sheet['A:C']  # 获取A列-C列全部单元格
cells = sheet[5]  # 获取第5行全部单元格
rows = sheet.rows# 获取所有行
#指定行和列范围
rows = sheet.iter_rows(min_row=1, max_row=5, min_col=1, max_col=4)
for row in rows:
    for cell in row:
        print('6===', cell.value)
