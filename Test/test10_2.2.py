from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "https://suninjuly.github.io/file_input.html"

try:
    browser= webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.NAME, "firstname")
    first_name.send_keys("John")

    last_name = browser.find_element(By.NAME, "lastname")
    last_name.send_keys("Doe")

    email = browser.find_element(By.NAME, "email")
    email.send_keys("jondoe@gmail.com")

    file_input = browser.find_element(By.NAME, "file")            
    file_input.send_keys("C:/Users/denis/Desktop/Selenium/chromedriver_mac_arm64/test.txt")

    button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button.click()
    
finally:
   time.sleep(10)
   browser.quit()