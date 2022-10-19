import openpyxl
workbook=openpyxl.load_workbook('新表.xlsx')
sheet=workbook.active
#插入行、列
# sheet.insert_cols(idx=1)#在第1列前插入一列
# sheet.insert_cols(idx=2,amount=3)#在第2列前插入三列
#删除行、列
# sheet.delete_cols(idx=1,amount=5)#从第1列开始删5列
#移动单元格 向右向下为正，向左向上为负
sheet.move_range('E4',rows=-3,cols=-3)
workbook.save('新表.xlsx')