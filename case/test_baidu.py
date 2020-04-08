from selenium import webdriver
from time import sleep
from util.getImage import crack
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
driver.get("https://www.bilibili.com/")
driver.maximize_window()
driver.implicitly_wait(3)
driver.find_element_by_css_selector('[class="name"]').click()
hands = driver.window_handles
print(hands)
sleep(3)
driver.switch_to.window(hands[1])
username = driver.find_element_by_id("login-username").send_keys("17691353745")
password = driver.find_element_by_id("login-passwd").send_keys('wangbaohong1227')
submit = driver.find_element_by_css_selector('[class="btn btn-login"]').click()
sleep(3)
#保存2张图片
crack(driver)
sleep(4)
# ac = ActionChains(driver)
# el = driver.find_element_by_css_selector('[class="geetest_slider_button"]')
# ac.drag_and_drop_by_offset(el,144.667,0).perform()
# js = "setTimeout(function(){debugger},5000)"
driver.close()
driver.switch_to.window(hands[0])
driver.close()