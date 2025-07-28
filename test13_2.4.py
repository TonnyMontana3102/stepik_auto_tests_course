from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import math

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser= webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)  

    button = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))

    book = browser.find_element(By.ID, "book").click()

    numb = browser.find_element(By.ID, "input_value").text
    
    inp_area = browser.find_element(By.ID, "answer")
    inp_area.send_keys(calc(numb))

    submit = browser.find_element(By.ID, "solve").click()

 #111111111111111111

finally:
   time.sleep(10)
   browser.quit()