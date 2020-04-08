from selenium import webdriver
from time import sleep
class Webdriver():
    def open_url(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://cdn1.python3.vip/files/selenium/test2.html")
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
    def radio(self):
        print("radio框")
        self.driver.find_element_by_css_selector('[value="小江老师"]').click()
        sleep(2)
    def checkbox(self):
        print("checkbox框")
        self.driver.find_element_by_css_selector('#s_checkbox input[value="小凯老师"]').click()
        self.driver.find_element_by_css_selector('#s_checkbox input[value="小江老师"]').click()
        sleep(2)
    def select(self):
        print("select框")
        from selenium.webdriver.support.ui import Select
        select = Select(self.driver.find_element_by_css_selector("#ss_single"))
        select.select_by_visible_text("小雷老师")
        sleep(2)
    def mul_select(self):
        print("多选框")
        from selenium.webdriver.support.ui import Select
        mul_select = Select(self.driver.find_element_by_css_selector('#ss_multi'))
        mul_select.deselect_all()
        self.driver.find_element_by_css_selector('#ss_multi option[value="小雷老师"]')
        self.driver.find_element_by_css_selector('#ss_multi option[value="小江老师"]')
        sleep(3)
    def close_driver(self):
        self.driver.close()
if __name__ == '__main__':
    w = Webdriver()
    w.open_url()
    w.mul_select()
    w.close_driver()



