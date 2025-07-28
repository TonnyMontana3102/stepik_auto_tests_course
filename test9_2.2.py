from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser= webdriver.Chrome()
    browser.get(link)

    text_for_math = browser.find_element(By.CSS_SELECTOR,"span#input_value")
    text_for_math = text_for_math.text
    x = calc(text_for_math)

    input_math = browser.find_element(By.CSS_SELECTOR, "input#answer")
    input_math.send_keys(x)

    im_robot = browser.find_element(By.CSS_SELECTOR, "input#robotCheckbox")
    im_robot.click()

    robot_rule = browser.find_element(By.CSS_SELECTOR,"input[value = robots]")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_rule)
    robot_rule.click()
    
    submit = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit)
    submit.click()

finally:
   time.sleep(10)
   browser.quit()