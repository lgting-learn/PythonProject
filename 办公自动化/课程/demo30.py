#教育机构 ：马士兵教育
#讲    师：杨淑娟
import  openpyxl
from  openpyxl.chart import  LineChart,Reference
workbook=openpyxl.load_workbook('新表.xlsx')
sheet=workbook['Sheet1']

#创建条形图的图表对象
chart=LineChart()
#数据的引用范围
data=Reference(worksheet=sheet,min_row=2,max_row=3,min_col=1,max_col=13)
#类别的引用范围
categories=Reference(sheet,min_row=1,min_col=2,max_col=13)

#将数据与类别添加到图表当中
chart.add_data(data,from_rows=True,titles_from_data=True)
chart.set_categories(categories)
#将图表插入到工作表中
sheet.add_chart(chart,'A12')
workbook.save('新表.xlsx')

