# 读取浏览器驱动，产生测试webdriver驱动对象
import os
from time import sleep
from selenium import webdriver
from UIautomation.atstudy.config.read_ini import ReadIni

# 工程路径
parent_path = os.path.dirname(os.path.dirname(__file__))
read = ReadIni()
url = read.get_value('url')


def get_chrome_driver():
    driver_path = parent_path+'/browserdriver/chromedriver.exe'
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(3)
    sleep(2)
    return driver


if __name__ == '__main__':
    get_chrome_driver()
