import time
import pytest


from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://practicetestautomation.com/")
driver.maximize_window()
driver.implicitly_wait(3)

action = ActionChains(driver)

practice_link = driver.find_element(By.XPATH, '//*[@id="menu-item-20"]/a')
action.move_to_element(practice_link).perform()
time.sleep(0.5)
practice_link.click()
driver.implicitly_wait(5)
