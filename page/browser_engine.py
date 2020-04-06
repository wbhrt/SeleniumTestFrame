import os
import time
from selenium import webdriver
from configparser import ConfigParser
from logs.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()
class BrowserEngine(object):
    dir = os.path.dirname(os.path.abspath("."))
    chrome_driver_path = dir + "/tools/chromedriver.exe"

    def __init__(self,driver):
        self.driver = driver
    def open_browser(self,driver):
        config = ConfigParser()
        path = os.path.dirname(os.path.abspath('.'))+'/config/config.ini'
        config.read(path)

        browser = config.get("browserType","browserName")
        logger.info("你选择的浏览器是:%s"%browser)
        url = config.get("testServer","url")
        logger.info("你要测试的网址是:%s"%url)

        if browser =="Chrome":
            driver = webdriver.Chrome(self.chrome_driver_path)
            logger.info("开启谷歌浏览器")
        driver.get(url)
        time.sleep(3)
        logger.info("最大化浏览器")
        driver.maximize_window()
        driver.implicitly_wait(10)
        return driver
    def quit_browser(self):
        logger.info("关闭浏览器")
        self.driver.quit()
