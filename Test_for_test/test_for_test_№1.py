from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest

link1 = "https://suninjuly.github.io/registration1.html"
link2 = "https://suninjuly.github.io/registration2.html"

def test(link):
        browser = webdriver.Chrome()
        browser.get(link)
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
        time.sleep(5)
        browser.quit()

class TestForTest(unittest.TestCase):   
    def test_link1(self):
          self.assertEqual(test(link1), "Congratulations! You have successfully registered!")
    def test_link2(self):
          self.assertEqual(test(link2), "Congratulations! You have successfully registered!")

if __name__ == "__main__":
    unittest.main()