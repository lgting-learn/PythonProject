#教育机构 ：马士兵教育
#讲    师：杨淑娟
import  openpyxl

#打开一个Excel表格
workbook=openpyxl.load_workbook('京东鞋子评论信息.xlsx')
print(workbook.sheetnames)

sheet=workbook['评论信息']    #获取指定的工作表
#sheet=workbook.active   #只有一个sheet的时候去使用
print(sheet.dimensions)  #获取工作表的尺寸
cell=sheet['A1']   #单元格
print(cell.value)

#获取某列连续单元格
cells=sheet['A1:A5']
for cell in cells:
    print(cell[0].value)
    print('----------------------')
print(cells)

