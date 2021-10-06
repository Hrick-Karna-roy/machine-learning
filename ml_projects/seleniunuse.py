import os
import selenium
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from PIL import Image
import io
import requests
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException

driver = webdriver.Chrome(ChromeDriverManager().install())
# driver.get('https://www.23andme.com/en-int/')
# # time.sleep(15)
# print(driver.title)
# driver.find_element_by_xpath('/html/body/div[9]/div/div/div/button[1]').click()
# print(driver.title)
# driver.find_element_by_xpath('/html/body/footer/section/div[1]/div[3]/ul/li[4]/a').click()
# print(driver.title)
# # driver.back()
# driver.find_element_by_xpath('/html/body/header/div/div[3]/div[1]/div/ul/li[1]/a').click()
# # driver.back()
# username_ele = driver.find_element_by_xpath('/html/body/main/div/div/div/div/form/div[1]/input')
# print(username_ele.is_displayed())
# print(username_ele.is_enabled())
# password_ele = driver.find_element_by_xpath('/html/body/main/div/div/div/div/form/div[2]/label')
# print(password_ele.is_displayed())
# print(password_ele.is_enabled())
# # driver.back()
# # driver.forward()
# p = driver.current_window_handle
# counter_window_handle = driver.window_handles
# print()
# for i in range(len(counter_window_handle)):
#     print(driver.title,end='\n\n')
#     if counter_window_handle[i] != p:
#         driver.switch_to.window(counter_window_handle[i])
#     else:
#         break
#
# print(driver.title)
# username_ele.send_keys('hrickkarnaroy@gmail.com')
# password_ele.send_keys('Hrick@123')
# time.sleep(15)
# driver.quit()
driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
#time.sleep(10)
username = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input=[name=’username’]")))
password = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input = [name = 'password']")))
print(username.is_displayed())
print(username.is_enabled())
print(password.is_displayed())
print(password.is_enabled())
username.clear()
username.send_keys("k__a__r__n__a__")
password.clear()
password.send_keys("13062001tesla")
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
# time.sleep(30)
# driver.close()
