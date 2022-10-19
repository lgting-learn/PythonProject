#教育机构 ：马士兵教育
#讲    师：杨淑娟
import  openpyxl

workbook=openpyxl.load_workbook('新表.xlsx')
sheet=workbook['Sheet1']
#设置行/列全部单元格宽高
#sheet.row_dimensions[2].height=50
sheet.column_dimensions['B'].width=20
workbook.save('新表.xlsx')