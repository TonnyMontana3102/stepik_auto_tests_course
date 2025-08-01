import time

# webdriver это и есть набор команд для управления браузером
from selenium import webdriver

# импортируем класс By, который позволяет выбрать способ поиска элемента
from selenium.webdriver.common.by import By

# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
driver = webdriver.Chrome()

# команда time.sleep устанавливает паузу в 5 секунд, чтобы мы успели увидеть, что происходит в браузере
time.sleep(2)

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
driver.get("https://x.com/home")
time.sleep(2)

# Метод find_element позволяет найти нужный элемент на сайте, указав путь к нему. Способы поиска элементов мы обсудим позже
# Метод принимает в качестве аргументов способ поиска и значение, по которому мы будем искать
# Ищем поле для ввода текста
textarea = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div/div/div[5]/section/div/div/div[2]/div/div/article")

# Напишем текст ответа в найденное поле
textarea.send_keys("get()")
time.sleep(2)

# Найдем кнопку, которая отправляет введенное решение
#submit_button = driver.find_element(By.CSS_SELECTOR, ".submit-submission")

# Скажем драйверу, что нужно нажать на кнопку. После этой команды мы должны увидеть сообщение о правильном ответе
#submit_button.click()
time.sleep(2)

# После выполнения всех действий мы должны не забыть закрыть окно браузера
driver.quit()