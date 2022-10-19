from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains

br = webdriver.Firefox()
sleep(2)
br.get('http://localhost/upload/forum.php')
sleep(2)
e = br.find_element_by_id('qmenu')
ActionChains(br).move_to_element(e).perform()
sleep(2)
js = "document.getElementById('qmenu_menu').style.display='block'"
br.execute_script(js)
sleep(2)
br.find_element_by_xpath('//*[@id="qmenu_menu"]/div/a[1]/strong').click()
sleep(2)
jj = "document.getElementById('qmenu_menu').style.display='display'"
br.execute_script(jj)
sleep(2)
br.find_element_by_xpath('//*[contains(@id, "username")]').send_keys('admin')
sleep(2)
br.find_element_by_xpath('//*[contains(@id, "password")]').send_keys('123456')
sleep(2)
br.find_element_by_xpath('/html/body/div[1]/div[2]/table/tbody/tr[2]/td[2]/'
                         'div[1]/div[1]/form/div/div[6]/table/tbody/tr/td[1]/'
                         'button/strong').submit()
sleep(7)
br.quit()
