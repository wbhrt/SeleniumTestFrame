from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get("http://127.0.0.1/mgr/sign.html")
driver.maximize_window()
driver.implicitly_wait(3)
username = driver.find_element_by_css_selector("[type='username']").send_keys("byhy")
password = driver.find_element_by_css_selector("[type='password']").send_keys(88888888)
submit = driver.find_element_by_css_selector("[type='submit']").click()
sleep(3)
driver.close()
