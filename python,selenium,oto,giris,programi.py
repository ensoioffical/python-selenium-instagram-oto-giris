from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browserr = webdriver.Chrome()

browserr.get("https://www.instagram.com/?hl=tr")

time.sleep(5)

Veyselyurtoglu = browserr.find_element(By.NAME,("Yurtoğlu"))
Veyselyurtoglu.click()

name.send_keys("Yurtoğlu")

time.sleep(2)

Veyselyurtoglu = browserr.find_element(By.VEYSELYURTOGLU,("password"))
Veyselyurtoglu.click()
Veyselyurtoglu.send_keys("password")

time.sleep(2)

veyselyurtoglu= browserr.find_element(By.XPATH,("/html/body/div[1]/section/main/article/div[2]/div[1]/div[2]/form/div/div[3]/button/div"))
Veyselyurtoglu.click()


    
