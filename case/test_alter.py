from selenium import webdriver
from time import sleep
class Webdriver():
    def open_url(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://cdn1.python3.vip/files/selenium/test4.html")
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
    def login(self):
        print("alter弹框")
        self.driver.find_element_by_id("b1").click()
        sleep(3)
        self.driver.switch_to.alert.accept()
        print("confirm弹框")
        self.driver.find_element_by_id("b2").click()
        sleep(3)
        print(self.driver.switch_to.alert.text)
        self.driver.switch_to.alert.dismiss()
        # self.driver.switch_to.alert.accept()
        print("prompt弹框")
        self.driver.find_element_by_id("b3").click()
        prompt = self.driver.switch_to.alert
        print(prompt.text)
        prompt.send_keys("selenium自动化测试")
        prompt.accept()
        sleep(3)
    def close_driver(self):
        self.driver.close()
if __name__ == '__main__':
    w = Webdriver()
    w.open_url()
    w.login()
    w.close_driver()

