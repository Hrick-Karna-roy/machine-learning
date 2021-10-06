import os
import selenium
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from PIL import Image
import io
import requests
from webdriver_manager.chrome import ChromeDriverManager
import wget
from selenium.common.exceptions import ElementClickInterceptedException
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
username = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[name='username']")))
password = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"input[name = 'password']")))
# print(username.is_displayed())
# print(username.is_enabled())
# print(password.is_displayed())
# print(password.is_enabled())
username.clear()
name = "k__a__r__n__a__" #input("enter the name : ")
passw = "13062001tesla" #input("enter tha password : ")
username.send_keys(name)
password.clear()
password.send_keys(passw)
driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]').click()
dnotnow = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//*[@id="react-root"]/section/main/div/div/div/div/button'))).click()
dnotnow2 = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//button[contains(text(),"Not Now")]'))).click()
# time.sleep(30)
# driver.close()
searchbox = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,"//input[@placeholder = 'Search']")))
searchbox.clear()

keyword = "#cat"
searchbox.send_keys(keyword)
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)
searchbox.send_keys(Keys.ENTER)
time.sleep(5)
driver.execute_script("window.scrollTo(0, 4000);")
images = driver.find_elements_by_tag_name('img')
print(len(images))
images = [image.get_attribute('src') for image in images]
print(len(images))
images = images[1::5]
print(len(images))


path = os.getcwd()
path = os.path.join(path, keyword[1:] + "s")
os.mkdir(path)

counter = 0   #for saving image by name
for image in images:
    save_as = os.path.join(path, keyword[1:] + str(counter) + ".jpg")
    wget.download(image, save_as)
    counter += 1
