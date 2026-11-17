import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

action = ActionChains(driver)

name_fld = driver.find_element(By.ID, 'name')
name_fld.click()
name_fld.send_keys("Jean")
time.sleep(0.5)

email_fld = driver.find_element(By.ID, 'email')
email_fld.click()
email_fld.send_keys("lazarito.jean.j@gmail.com")
time.sleep(0.5)

phone_fld = driver.find_element(By.ID, 'phone')
phone_fld.click()
phone_fld.send_keys("12345")
time.sleep(0.5)

textarea_fld = driver.find_element(By.ID, 'textarea')
textarea_fld.click()
textarea_fld.send_keys("Naga City")
time.sleep(0.5)

gender = driver.find_element(By.ID, 'female')
gender.click()
time.sleep(0.5)

saturday = driver.find_element(By.ID, 'saturday')
saturday.click()
time.sleep(0.5)

thursday = driver.find_element(By.ID, 'thursday')
thursday.click()
time.sleep(0.5)

country_fld = driver.find_element(By.ID, 'country')
country_fld.click()
time.sleep(0.5)
selectCountry = Select(country_fld)
# action.move_to_element(selectCountry.select_by_value('france')).perform()
selectCountry.select_by_value('germany')
time.sleep(0.5)

color_dropdown = driver.find_element(By.ID, 'colors')
time.sleep(0.5)
selectColor = Select(color_dropdown)
selectColor.select_by_value("blue")
time.sleep(0.5)

animals_dropdown = driver.find_element(By.ID, 'animals')
time.sleep(0.5)
selectAnimal = Select(animals_dropdown)
selectAnimal.select_by_value("deer")
time.sleep(0.5)

datepicker1_fld = driver.find_element(By.ID, 'datepicker')
datepicker1_fld.click()
time.sleep(0.5)
date1 = driver.find_element(By.LINK_TEXT, '11')
date1.click()
time.sleep(0.5)


datepicker2_fld = driver.find_element(By.ID, 'txtDate')
datepicker2_fld.click()
time.sleep(0.5)
date2 = driver.find_element(By.LINK_TEXT, '17')
date2.click()
time.sleep(0.5)

date_picker = driver.find_element(By.CLASS_NAME, 'date-picker-box')
action.move_to_element(date_picker).perform()
time.sleep(0.5)

r1_datepicker3_fld = driver.find_element(By.ID, 'start-date')
time.sleep(0.5)
r1_datepicker3_fld.send_keys("2021-03-31")
time.sleep(1)

# r1_dd= action.move_by_offset(339, 671)
# r1_dd.click()
# r1_dd.send_keys("2021-03-31")
# time.sleep(0.5)
# r1_dd.send_keys("11")
# time.sleep(0.5)

# r1_mm= action.move_by_offset(367, 665)
# r1_mm.click()
# r1_mm.send_keys("11")
# r1_datepicker3_fld.send_keys("2021-03-31")
# time.sleep(2)
#
# r2_datepicker3_fld = driver.find_element(By.ID, 'end-date')
# action.move_to_element(r1_datepicker3_fld).perform()
# time.sleep(0.5)
# r2_datepicker3_fld.click()
# time.sleep(0.5)
# r2_datepicker3_fld.send_keys("2021-04-09")
# time.sleep(2)
#
# submit_date=driver.find_element(By.CLASS_NAME, 'submit-btn')
# submit_date.click()
# time.sleep(1)
#
# home_txt = driver.find_element(By.LINK_TEXT, 'Home')
# action.move_to_element(home_txt).perform()
# time.sleep(1)
# home_txt.click()
# time.sleep(0.5)
#
# posts_atom_txt = driver.find_element(By.LINK_TEXT, 'Posts (Atom)')
# action.move_to_element(posts_atom_txt).perform()
# time.sleep(0.5)
# posts_atom_txt.click()
# time.sleep(3)
# driver.close()
# driver.switch_to.window(driver.current_window_handle)
# time.sleep(2)
