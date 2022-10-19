from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


br = webdriver.Edge()  # 启动浏览器
sleep(2)
br.get("https://mail.163.com")  # 打开论坛首页
sleep(2)
br.maximize_window()  # 浏览器最大化
sleep(2)
br.refresh()  # 刷新页面
sleep(2)
br.back()  # 往后退一页
sleep(2)
br.forward()  # 往前进一页
sleep(2)
i = br.find_element(By.XPATH, '//body/div[2]/div[3]/div[1]/div/div[4]/div[1]/div[1]/iframe')  # 切换iframe
br.switch_to.frame(i)
br.find_element(By.XPATH, "//*[@name='email']").send_keys("admin")  # 定位到用户名输入框，输入admin
sleep(2)
br.find_element(By.XPATH, "//*[@name='password']").send_keys("123456")  # 定位到密码输出框，输入123456
sleep(2)
br.find_element(By.XPATH, "//*[@name='password']").clear()  # 清空文本print(br.page_source)
print(br.title)  # 获取标题、获取源代码print(br.page_source)
print(br.page_source)
br.find_element(By.CSS_SELECTOR, "#dologin").click()  # 点击登录
sleep(2)
br.find_element(By.LINK_TEXT, "退出").click()  # 点击退出
sleep(2)
br.quit()  # 退出

'''八种元素定位方法：目前有新的写法。
    find_element_by_id(‘xx’)：id定位，根据元素的id属性值定位，最为方便且唯一，但有可能不存在，也可能动态生成
    find_element_by_name(‘xx’)：name定位，根据元素的name属性值定位，但通常不唯一
    find_element_by_class_name(‘xx’)：class定位，根据元素的class属性值定位，但可能受JS影响动态变化   
    find_element_by_tag_name(‘xx’)：tag name定位，根据元素的标签名定位，但很少唯一    
    find_element_by_link_text(‘xx’)：根据链接文本进行定位。只能针对链接元素（a元素）    
    find_element_by_partial_link_text(‘xx’)：根据链接文本的部分文本内容进行定位。    
    find_element_by_xpath(‘xx’)：根据元素的xpath表达式来完成定位，可以准确定位任何元素，但需要熟练掌握xpath语法    
    find_element_by_css_selector(‘xx’)：根据元素的css选择器来完成定位，可以准确定位任何元素，但需要熟练掌握css选择器'''

'''Xpath是一种在XML文档中定位元素的语言。
    （1）使用绝对路径的方式来定位    
        指的是从网页的HTML代码结构的最外层一层层的写到需要被定位的页面元素为止。        
        绝对路径起始于/，每一层都被/所分割。        
        Eg:/html/body/div[2]/form/input[3]    
        注解：可以用中括号选择分支，div[2]代表的是当前层级下的第二个div标签；
    （2）使用相对路径的方式来定位   
        不是从根目录写起，而是从网页文本的任意目录开始写。        
        相对路径起始于//，//所表示的含义是“任意目录下”       
        Eg://input[@id=’kw’]'''

'''CSS选择器可用于定位页面元素。
    常用的几种选择器：    
        类选择器——》.xxx 选择class属性为xxx的元素        
        id选择器——》#xxx 选择id属性为xxx的元素        
        元素选择器——》xxx 选择标签名为xxx的元素        
        属性选择器——》[yyy=’bbb’]选择yyy属性取值为bbb的元素        
        在CSS里标识层级关系使用的是>（xpath里使用的是/）        
        Eg:div#xx1>input.yy2
    
    注意：对于CSS的属性值来说，可以加引号也可以不加，对于xpath的属性值来讲，需要加上引号，否则报错。    
        find_element_by_css_selector(‘aa.xx’)       
        find_element_by_css_selector(‘aa#xx’)       
        find_element_by_css_selector(‘aa[yy=xx]’)    
        find_element_by_css_selector(‘aa[yy=”xx”]’)    
        find_element_by_css_selector(“aa[yy=’xx’]”)   
        find_element_by_css_selector(“aa[yy=xx]”)       
        find_element_by_xpath(‘//aa[@class=”xx”]’)      
        find_element_by_xpath(‘//aa[@id=”xx”]’)     
        find_element_by_xpath(‘//aa[@yy=”xx”]’)     
        find_element_by_xpath(“//aa[@yy=’xx’]”)'''
