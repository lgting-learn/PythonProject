from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

br = webdriver.Firefox()

br.get('http://localhost/sourcePage/s1/singleselect.html')

# 定位下拉列表元素（Select()类用于检查定位到的元素是否为下拉列表，如果不是抛出异常，如果是则获取该下拉列表元素进行返回）

s=Select(br.find_element(By.ID, "education"))

# 三种定位下拉列表选项的方法

# 通过value属性的取值选择选项
s.select_by_value("3")  # 博士
sleep(2)

# 通过选项的文本内容选择选项
s.select_by_visible_text("大学")
sleep(2)

# 通过选择项的编号（索引号）选择选项
s.select_by_index(0)  # 高中
sleep(2)

# 利用循环的方式依次选择选项：
for i in s.options:
    i.click()

sleep(2)
br.quit()