from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browserr = webdriver.Chrome()

browserr.get("https://www.instagram.com/?hl=tr")

time.sleep(5)

name = browserr.find_element(By.NAME,("username"))
name.click()

name.send_keys("username")

time.sleep(2)

name2 = browserr.find_element(By.NAME,("password"))
name2.click()
name2.send_keys("password")

time.sleep(2)

name3 = browserr.find_element(By.XPATH,("/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div"))
name3.click()


    
