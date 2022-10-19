#教育机构 ：马士兵教育
#讲    师：杨淑娟
'''课堂小案例：
 打开京东鞋子评论信息.xlsx，找到41码的所有鞋子评论数据
 输出这些单元格的坐标，比较A1,C10等
'''
import  openpyxl
workbook=openpyxl.load_workbook('京东鞋子评论信息.xlsx')  #打开Excel文件
sheet=workbook['评论信息']  #获取sheet工作表
#41码的鞋子共几双
cols=sheet['D']   #获取D列
count=0
for col in cols:
   if col.value=='41':
       count+=1
       print('D'+str(col.row))

print('41码的鞋子一共销售了',count,'双')
