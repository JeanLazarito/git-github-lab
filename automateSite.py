import time

from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()

action = ActionChains(driver)

right_click_btn = driver.find_element(By.CLASS_NAME, 'context-menu-one.btn.btn-neutral')
action.context_click(right_click_btn).perform()
time.sleep(2)

edit_option = driver.find_element(By.XPATH, '/html/body/ul/li[1]')
action.click(edit_option).perform()
time.sleep(1)
driver.switch_to.alert.accept()
time.sleep(2)

# action.context_click(right_click_btn).perform()
# cut_option = driver.find_element(By.XPATH, '/html/body/ul/li[2]')
# action.click(cut_option).perform()
# time.sleep(1)
# driver.switch_to.alert.accept()
# time.sleep(2)
#
# action.context_click(right_click_btn).perform()
# copy_option = driver.find_element(By.XPATH, '/html/body/ul/li[3]')
# action.click(copy_option).perform()
# time.sleep(1)
# driver.switch_to.alert.accept()
# time.sleep(2)
#
# action.context_click(right_click_btn).perform()
# paste_option= driver.find_element(By.XPATH, '/html/body/ul/li[4]')
# action.click(paste_option).perform()
# time.sleep(1)
# driver.switch_to.alert.accept()
# time.sleep(2)
#
# action.context_click(right_click_btn).perform()
# delete_option= driver.find_element(By.XPATH, '/html/body/ul/li[5]')
# action.click(delete_option).perform()
# time.sleep(1)
# driver.switch_to.alert.accept()
# time.sleep(2)
#
# action.context_click(right_click_btn).perform()
# quit_option = driver.find_element(By.XPATH, '/html/body/ul/li[7]')
# action.click(quit_option).perform()
# time.sleep(1)
# driver.switch_to.alert.accept()
# time.sleep(3)

move_to_link = driver.find_element(By.LINK_TEXT, 'Example code: Simple Context Menu')
action.move_to_element(move_to_link).perform()
time.sleep(2)
action.click(move_to_link).perform()
time.sleep(3)
driver.quit()
