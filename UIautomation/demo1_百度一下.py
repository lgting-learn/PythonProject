from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from time import sleep

browser = webdriver.Chrome()  # 启动浏览器
sleep(2)
# browser.implicitly_wait(10)  # 隐式等待，等待所有页面加载完成，完成不了报错。
browser.get("https://www.baidu.com/")  # 打开百度页面
# 通过js的方式新建标签页：
# js = "window.open('{url}')"
# browser.execute_script(js)
# browser.find_element(By.LINK_TEXT, '百度').click()
sleep(2)
browser.find_element(By.ID, "kw").send_keys("selenium")  # 在搜索框输入selenium
sleep(2)
# browser.find_element(By.ID, "su").click()  # 点击“百度一下”，click更强调独立性。
# 如图，有序列表<li>和无序列表<ul>组成了一个form表单，登录按钮属性为submit。type = submit
# 在form表单中，所有数据是一起提交的。提交任何一个元素，就提交了整个表单。
# 可以简化为：
# e = browser.find_element(By.ID, 'su')
# e.submit
browser.find_element(By.ID, 'su').submit()
sleep(2)
browser.quit()
