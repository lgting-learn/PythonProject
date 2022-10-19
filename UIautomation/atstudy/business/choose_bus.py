from time import sleep
from selenium.webdriver import ActionChains
from UIautomation.atstudy.config.driver import get_chrome_driver
from UIautomation.atstudy.config.findelement import FindElement
from UIautomation.atstudy.config.read_ini import ReadIni


def choose(username, password, number):
    read = ReadIni()
    driver = get_chrome_driver()
    find = FindElement(driver)

    try:
        find.get_element(node='login', key='user_login').click()
        find.get_element(node='login', key='user_name').send_keys(username)
        find.get_element(node="login", key="user_password").send_keys(password)
        find.get_element(node="login", key="login_button").click()
        sleep(2)
        find.get_element(node="choose_bus", key="chooseCentre").click()
        sleep(3)
        find.get_element(node="choose_bus", key="priceOrder").click()
        sleep(3)
        find.get_element(node="choose_bus", key="priceOrder").click()
        sleep(3)
        find.get_element(node="choose_bus", key="secondLesson").click()
        # lesson_xpath = "//*[@id='__layout']/div/div[2]/div/div[2]/div[2]/div["+str(number)+"]/div[3]/button"
        # driver.find_element_by_xpath(lesson_xpath).click()
        sleep(2)
        find.get_element(node="choose_bus", key="startLearn").click()
        sleep(2)
        result = find.get_element(node="choose_bus", key="proof")
        sleep(2)
        if result is None:
            return False
        else:
            return True
    except Exception as e:
        print("错误明细：", e)
        return False
    finally:
        driver.quit()


if __name__ == '__main__':
    choose('19999999999', 'a12345', 3)
