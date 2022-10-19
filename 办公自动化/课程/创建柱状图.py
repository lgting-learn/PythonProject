# 教育机构 ：马士兵教育
# 讲    师：杨淑娟
import openpyxl
from openpyxl.chart import BarChart, Reference

workbook = openpyxl.load_workbook('新表.xlsx')
sheet = workbook['Sheet1']

# 创建柱状图
chart = BarChart()
# 数据的引用范围
data = Reference(worksheet=sheet, min_row=1, max_row=13, min_col=1, max_col=2)
# 类别的引用范围
categories = Reference(sheet, min_row=2, max_row=13, min_col=1)

# 将数据与类别添加到图表当中
chart.add_data(data, titles_from_data=True)
chart.set_categories(categories)
# 将图表插入到工作表中
sheet.add_chart(chart, 'F12')
workbook.save('新表.xlsx')
