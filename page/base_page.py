import os
import time
from logs.logger import Logger

logger = Logger(logger="BasePage").getlog()
class BasePage(object):
    def __init__(self,driver):
        self.driver = driver

    def quit_browser(self):
        self.driver.quit()

    def forward(self):
        self.driver.forward()

    def back(self):
        self.driver.back()

    def wait(self,time):
        self.driver.implicitly_wait(time)

    def close_browser(self):
        try:
            self.driver.close()
        except NameError as e:
            print(e)

    def get_windows_img(self):
        path = os.path.dirname(os.path.abspath("."))+'/screenshots/'
        t = time.strftime("%Y%m%d%H%H",time.localtime(time.time()))
        screen_name = path +t +".png"
        try:
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("保存截图到screenshots文件夹")
        except NameError as e:
            logger.info("截图失败的原因：%s"%e)
            self.get_windows_img()
