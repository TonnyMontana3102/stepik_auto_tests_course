from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try: 
    link = "https://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name']")
    input1.send_keys("John")
    input2 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name']")
    input2.send_keys("Doe")
    input3 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email']")
    input3.send_keys("New-York123@gmail.com")
    input4 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your phone:']")
    input4.send_keys("911")
    input5 = browser.find_element(By.CSS_SELECTOR, "input[placeholder='Input your address:']")
    input5.send_keys("Germany, Tokio, 123")

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()