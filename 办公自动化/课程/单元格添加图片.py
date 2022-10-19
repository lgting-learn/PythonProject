# 教育机构 ：马士兵教育
# 讲    师：杨淑娟
import openpyxl
from openpyxl.drawing.image import Image

workbook = openpyxl.load_workbook('新表.xlsx')
sheet = workbook.create_sheet('imagesheet')
# 单元格添加图片
logo = Image('logo.png')
logo.height = 90
logo.width = 100
sheet.add_image(logo, 'A1')
workbook.save('新表.xlsx')
