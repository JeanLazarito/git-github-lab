import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

action = ActionChains(driver)

for li_txt in ['Udemy Courses', 'Online Trainings', 'Blog', 'PlaywrightPractice']:
    nav_link = driver.find_element(By.LINK_TEXT, li_txt)
    action.move_to_element(nav_link).perform()
    time.sleep(0.8)
    nav_link.click()
    time.sleep(0.5)
    driver.back()
    time.sleep(1)

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

driver.find_element(By.ID, 'female').click()
time.sleep(0.5)

driver.find_element(By.ID, 'saturday').click()
time.sleep(0.5)

driver.find_element(By.ID, 'thursday').click()
time.sleep(0.5)

country_fld = driver.find_element(By.ID, 'country')
action.move_to_element(country_fld).perform()
time.sleep(0.5)
Select(country_fld).select_by_value('germany')

time.sleep(0.5)
Select(driver.find_element(By.ID, 'colors')).select_by_value("blue")
time.sleep(0.5)

Select(driver.find_element(By.ID, 'animals')).select_by_value("deer")
time.sleep(0.5)

driver.find_element(By.ID, 'datepicker').click()
time.sleep(0.5)
driver.find_element(By.LINK_TEXT, '11').click()
time.sleep(0.5)

driver.find_element(By.ID, 'txtDate').click()
time.sleep(0.5)
driver.find_element(By.LINK_TEXT, '17').click()
time.sleep(0.5)

action.move_to_element(driver.find_element(By.CLASS_NAME, 'date-picker-box')).perform()
time.sleep(0.5)

driver.find_element(By.ID, 'start-date').send_keys("11/15/2026")
time.sleep(0.5)

driver.find_element(By.ID, 'end-date').send_keys("11/20/2021")
time.sleep(0.5)

driver.find_element(By.CLASS_NAME, 'submit-btn').click()
time.sleep(0.5)

action.scroll_to_element(driver.find_element(By.XPATH, '//*[@id="Blog1"]/div[1]/div/div/div/div/div[3]/div[1]')).perform()
time.sleep(0.5)

home_txt = driver.find_element(By.XPATH, '//*[@id="blog-pager"]/a')
action.scroll_to_element(home_txt).perform()
time.sleep(1)
action.move_to_element(home_txt).perform()
time.sleep(0.5)
home_txt.click()
time.sleep(2)

posts_atom_txt = driver.find_element(By.XPATH, '//*[@id="Blog1"]/div[4]/div/a')
action.scroll_to_element(posts_atom_txt).perform()
time.sleep(1)
action.move_to_element(posts_atom_txt).perform()
time.sleep(0.5)
posts_atom_txt.click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[-1])
driver.close()
driver.switch_to.window(driver.window_handles[0])
time.sleep(2)

driver.find_element(By.ID, 'singleFileInput').send_keys(r"C:\Users\Jean Lazarito\Pictures\ㅤ ㅤㅤㅤ★    woooooooosh, now u're gay—_.jpg")
time.sleep(0.5)
btn_single_file_upload = driver.find_element(By.CSS_SELECTOR, '#singleFileForm button')
action.move_to_element(btn_single_file_upload).perform()
time.sleep(0.5)
btn_single_file_upload.click()
time.sleep(1)

multiple_file_upload = driver.find_element(By.ID, 'multipleFilesInput')
multiple_file_upload.send_keys(r"C:\Users\Jean Lazarito\Pictures\ㅤ ㅤㅤㅤ★    woooooooosh, now u're gay—_.jpg")
time.sleep(0.5)
multiple_file_upload.send_keys(r"C:\Users\Jean Lazarito\Pictures\470595535_122148789314360468_4434360845270132450_n.jpg")
time.sleep(0.5)
btn_multiple_file_upload = driver.find_element(By.CSS_SELECTOR, '#multipleFilesForm button')
action.move_to_element(btn_multiple_file_upload).perform()
time.sleep(0.5)
btn_multiple_file_upload.click()
time.sleep(1)


action.scroll_to_element(driver.find_element(By.XPATH, '//*[@id="HTML8"]')).perform()
time.sleep(1)
for chk in range (1, 6):
    chkPage1 = driver.find_element(By.XPATH, f'//*[@id="productTable"]/tbody/tr[{chk}]/td[4]/input')
    action.move_to_element(chkPage1).perform()
    time.sleep(0.5)
    chkPage1.click()
    time.sleep(0.5)
    if chk == 5:
        for page in range (2, 5):
            driver.find_element(By.XPATH, f'//*[@id="pagination"]/li[{page}]/a').click()
            time.sleep(0.5)
            if page == 4:
                for chk1 in range(1, 6):
                    chkPage4 = driver.find_element(By.XPATH, f'//*[@id="productTable"]/tbody/tr[{chk1}]/td[4]/input')
                    action.move_to_element(chkPage4).perform()
                    time.sleep(0.5)
                    chkPage4.click()
                    time.sleep(0.5)

wiki_input = driver.find_element(By.ID, 'Wikipedia1_wikipedia-search-input')
action.move_to_element(wiki_input).perform()
time.sleep(0.5)
wiki_input.send_keys("Shrek", Keys.ENTER)
time.sleep(0.5)
action.move_to_element(driver.find_element(By.LINK_TEXT, 'Shrek')).perform()
time.sleep(0.5)
action.move_to_element(driver.find_element(By.LINK_TEXT, 'Shrek (franchise)')).perform()
time.sleep(0.5)
action.move_to_element(driver.find_element(By.LINK_TEXT, 'Shrek Forever After')).perform()
time.sleep(0.5)
shrek_2 = driver.find_element(By.LINK_TEXT, 'Shrek 2')
action.move_to_element(shrek_2).perform()
time.sleep(0.5)
shrek_2.click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[-1])
driver.close()
driver.switch_to.window(driver.window_handles[0])
time.sleep(0.5)

dynamic_button = driver.find_element(By.XPATH, '//*[@id="HTML5"]/div[1]/button')
action.move_to_element(dynamic_button).perform()
time.sleep(1)
dynamic_button.click()
time.sleep(0.5)
dynamic_button.click()
time.sleep(0.5)
dynamic_button.click()
time.sleep(0.5)

driver.find_element(By.ID, 'alertBtn').click()
time.sleep(0.5)
driver.switch_to.alert.accept()
time.sleep(0.5)

driver.find_element(By.ID, 'confirmBtn').click()
time.sleep(0.5)
driver.switch_to.alert.dismiss()
time.sleep(0.5)

driver.find_element(By.ID, 'promptBtn').click()
time.sleep(0.5)
driver.switch_to.alert.send_keys("Shrek")
time.sleep(0.5)
driver.switch_to.alert.accept()
time.sleep(0.5)

new_tab_btn = driver.find_element(By.XPATH, '//*[@id="HTML4"]/div[1]/button')
action.move_to_element(new_tab_btn).perform()
time.sleep(1)
new_tab_btn.click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[-1])
driver.close()
driver.switch_to.window(driver.window_handles[0])
time.sleep(0.5)

popup_btn = driver.find_element(By.ID, 'PopUp')
action.move_to_element(popup_btn).perform()
time.sleep(1)
popup_btn.click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[-1])
driver.close()
driver.switch_to.window(driver.window_handles[-1])
driver.close()
driver.switch_to.window(driver.window_handles[0])
time.sleep(0.5)

action.move_to_element(driver.find_element(By.CLASS_NAME, 'dropbtn')).perform()
time.sleep(1)
action.move_to_element(driver.find_element(By.LINK_TEXT, 'Mobiles')).perform()
time.sleep(0.5)
laptops_link = driver.find_element(By.LINK_TEXT, 'Laptops')
action.move_to_element(laptops_link).perform()
time.sleep(0.5)
laptops_link.click()
time.sleep(0.5)

field1_txt = driver.find_element(By.ID, 'field1')
action.move_to_element(field1_txt).perform()
time.sleep(0.5)
copy_btn = driver.find_element(By.XPATH, '//*[@id="HTML10"]/div[1]/button')
action.move_to_element(copy_btn).perform()
time.sleep(0.5)
action.double_click(copy_btn).perform()
time.sleep(1)

draggable = driver.find_element(By.ID, 'draggable')
action.move_to_element(draggable).perform()
time.sleep(1)
action.drag_and_drop(draggable, driver.find_element(By.ID, 'droppable')).perform()
time.sleep(1)

slider_handles = driver.find_elements(By.CLASS_NAME, 'ui-slider-handle')
action.move_to_element(slider_handles[0]).perform()
time.sleep(1)
action.drag_and_drop_by_offset(slider_handles[0], 50, 0).perform()
time.sleep(1)
action.drag_and_drop_by_offset(slider_handles[1], -30, 0).perform()
time.sleep(1)

action.move_to_element(driver.find_element(By.XPATH, '//*[name()="circle"]')).perform()
time.sleep(0.5)
action.move_to_element(driver.find_element(By.XPATH, '//*[name()="rect"]')).perform()
time.sleep(0.5)
action.move_to_element(driver.find_element(By.XPATH, '//*[name()="polygon"]')).perform()
time.sleep(0.5)

driver.find_element(By.ID, 'comboBox').click()
time.sleep(0.5)
for i in range(1, 11):
    action.move_to_element(driver.find_element(By.XPATH, f'//*[@id="dropdown"]/div[{i}]')).perform()
    time.sleep(0.2)

item_90= driver.find_element(By.XPATH, '//*[@id="dropdown"]/div[90]')
action.move_to_element(item_90).perform()
time.sleep(0.5)
item_90.click()
time.sleep(0.5)


action.move_to_element(driver.find_element(By.ID, 'samsung')).perform()
time.sleep(0.5)
action.move_to_element(driver.find_element(By.ID, 'realme')).perform()
time.sleep(0.5)
action.move_to_element(driver.find_element(By.ID, 'moto')).perform()
time.sleep(0.5)

for laptop_id in ['apple', 'lenovo', 'dell']:
    laptop_link = driver.find_element(By.ID, laptop_id)
    action.move_to_element(laptop_link).perform()
    time.sleep(0.5)
    laptop_link.click()
    time.sleep(0.5)
    driver.back()
    time.sleep(0.5)

for li in range(1,9):
    broken_link = driver.find_element(By.XPATH, f'//*[@id="broken-links"]/a[{li}]')
    action.move_to_element(broken_link).perform()
    time.sleep(0.5)
    broken_link.click()
    time.sleep(0.5)
    driver.back()
    time.sleep(0.5)

for secNum in range(1,4):
    action.move_to_element(driver.find_element(By.ID, f'section{secNum}')).perform()
    time.sleep(0.5)
    driver.find_element(By.ID, f'input{secNum}').send_keys(f"Section {secNum}")
    time.sleep(0.5)
    driver.find_element(By.ID, f'btn{secNum}').click()
    time.sleep(0.5)


shadow_host = driver.find_element(By.ID, 'shadow_host')
action.move_to_element(shadow_host).perform()
time.sleep(1)
shadow_root = shadow_host.shadow_root
shadow_root.find_element(By.CSS_SELECTOR, 'input[type="text"]').send_keys("Lisoda ba ani")
time.sleep(0.5)
shadow_root.find_element(By.CSS_SELECTOR, 'input[type="checkbox"]').click()
time.sleep(0.5)
shadow_root.find_element(By.CSS_SELECTOR, 'input[type="file"]').send_keys(r"C:\Users\Jean Lazarito\Pictures\470595535_122148789314360468_4434360845270132450_n.jpg")
time.sleep(0.5)

youtube = driver.find_element(By.LINK_TEXT, 'Youtube')
action.move_to_element(youtube).perform()
time.sleep(0.5)
youtube.click()
time.sleep(0.5)
driver.back()
time.sleep(0.5)

for li_footer in range(1, 4):
    li_foot = driver.find_element(By.XPATH, f'//*[@id="PageList1"]/div/ul/li[{li_footer}]/a')
    action.move_to_element(li_foot).perform()
    time.sleep(0.5)

driver.find_element(By.XPATH, '//*[@id="PageList1"]/div/ul/li[2]/a').click()
time.sleep(0.5)

input1 = driver.find_element(By.ID, 'input1')
action.move_to_element(input1).perform()
time.sleep(0.5)
input1.send_keys("Shrek")
time.sleep(0.5)

driver.find_element(By.ID, 'checkbox1').click()
time.sleep(0.5)

toggle_input = driver.find_element(By.ID, 'toggleInput')
action.move_to_element(toggle_input).perform()
time.sleep(0.5)
toggle_input.click()
time.sleep(0.5)
driver.find_element(By.ID, 'input2').send_keys("Shrek 2")
time.sleep(0.5)

toggle_checkbox = driver.find_element(By.ID, 'toggleCheckbox')
action.move_to_element(toggle_checkbox).perform()
time.sleep(0.5)
toggle_checkbox.click()
time.sleep(0.5)
driver.find_element(By.ID, 'checkbox2').click()
time.sleep(0.5)

load_ajax = driver.find_element(By.ID, 'loadContent')
action.move_to_element(load_ajax).perform()
time.sleep(0.5)
load_ajax.click()
time.sleep(3)
action.scroll_to_element(driver.find_element(By.XPATH, '//*[@id="ajaxContent"]/p')).perform()
time.sleep(2)

driver.back()
time.sleep(1)

driver.find_element(By.XPATH, '//*[@id="PageList1"]/div/ul/li[3]/a').click()
time.sleep(0.5)

text_fld = driver.find_element(By.ID, 'inputText')
action.move_to_element(text_fld).perform()
time.sleep(0.5)
text_fld.click()
text_fld.send_keys("Shrek the Third")
time.sleep(0.5)

gen_txt = driver.find_element(By.ID, 'generateTxt')
action.move_to_element(gen_txt).perform()
time.sleep(0.5)
gen_txt.click()
time.sleep(0.5)
txt_link = driver.find_element(By.ID, 'txtDownloadLink')
action.move_to_element(txt_link).perform()
time.sleep(0.5)
txt_link.click()
time.sleep(1)

gen_pdf = driver.find_element(By.ID, 'generatePdf')
action.move_to_element(gen_pdf).perform()
time.sleep(0.5)
gen_pdf.click()
time.sleep(0.5)
pdf_link = driver.find_element(By.ID, 'pdfDownloadLink')
action.move_to_element(pdf_link).perform()
time.sleep(0.5)
pdf_link.click()
time.sleep(1)

open_pdf_btn = driver.find_element(By.XPATH, '//button[text()="Download PDF File"]')
action.scroll_to_element(open_pdf_btn).perform()
time.sleep(1)
action.move_to_element(open_pdf_btn).perform()
time.sleep(0.5)
open_pdf_btn.click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[-1])
driver.close()
driver.switch_to.window(driver.window_handles[0])
time.sleep(0.5)
driver.back()

driver.find_element(By.LINK_TEXT, 'Home').click()
time.sleep(2)

driver.quit()
