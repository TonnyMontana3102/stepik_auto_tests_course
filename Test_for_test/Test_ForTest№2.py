from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

link1 = "https://suninjuly.github.io/registration1.html"
link2 = "https://suninjuly.github.io/registration2.html"

def testik(link):
	browser = webdriver.Chrome()
	browser.get(link)
	browser.implicitly_wait(3)
	input1 = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.first_class > input")
	input1.send_keys("John")
	input2 = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.second_class > input")
	input2.send_keys("Doe")
	input3 = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.first_block > div.form-group.third_class > input")
	input3.send_keys("New-York123@gmail.com")
	input4 = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.second_block > div.form-group.first_class > input")
	input4.send_keys("911")
	input5 = browser.find_element(By.CSS_SELECTOR, "body > div > form > div.second_block > div.form-group.second_class > input")
	input5.send_keys("Germany, Tokio, 123")
		# Отправляем заполненную форму
	button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
	button.click()
	browser.quit()
	return("Congratulations! You have successfully registered!")
		

def test1():
	assert testik(link1) == "Congratulations! You have successfully registered!"
def test2():
	assert testik(link2) == "Congratulations! You have successfully registered!"   

       
    
if __name__ == "__main__":
	pytest.main()