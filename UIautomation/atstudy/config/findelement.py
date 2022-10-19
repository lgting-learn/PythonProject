# 封装查找元素的方法
import os
from time import sleep
from UIautomation.atstudy.config.driver import get_chrome_driver
from UIautomation.atstudy.config.read_ini import ReadIni


class FindElement:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, file=None, node=None, key=None):
        if file is None:
            file = os.path.dirname(os.path.dirname(__file__))+'/business/LocalElement.ini'

        if node is None:
            node = 'login'

        read = ReadIni(file, node)
        data = read.get_value(key)
        by = data.split('>')[0]
        value = data.split('>')[1]

        try:
            if by == 'id':
                return self.driver.find_element_by_id(value)
            elif by == 'name':
                return self.driver.find_element_by_name(value)
            elif by == 'className':
                return self.driver.find_element_by_class_name(value)
            elif by == 'link_text':
                return self.driver.find_element_by_link_text(value)
            elif by == 'xpath':
                return self.driver.find_element_by_xpath(value)
        except:
            return None

    def scrollbottom(self):
        self.driver.set_window_size(600, 600)
        sleep(2)
        js = 'window.scrollTo(0, 600);'
        self.driver.execute_script(js)


if __name__ == '__main__':
    parent_path = os.path.dirname(os.path.dirname(__file__))
    driver = get_chrome_driver()
    test = FindElement()
    print(test.get_element(parent_path+'/business/LocalElement.ini', 'login', 'user_login'))
