import openpyxl

workbook = openpyxl.load_workbook('京东鞋子评论信息.xlsx')
sheet=workbook['评论信息']
cols=sheet['D']
count=0
for col in cols:
    if(col.value=='41'):
        count+=1
        print(str(col.row))
print('41码的鞋子卖了',count,'双')