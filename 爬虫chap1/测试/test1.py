#html数据筛选的三种方法：
# （1）正则表达式
# 对短字符进行处理，与字符串处理的内置函数配套使用
import re#导入re模块

# （2）xpath表达式
# 更简单的处理html文档
from lxml import etree
# （3）BeautifulSoup
# bs4更简单的处理html文档，简单且功能强大，爬虫常用