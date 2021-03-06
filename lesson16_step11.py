from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome(executable_path="D:\WebDrvers\Chrome\chromedriver_win32\chromedriver.exe")
    browser.get(link)

    # Ваш код, который заполняет обязательные поля

    def text_inputer(element):
        n = 0
        n = n + 1
        element.send_keys("Мой ответ" + str(n))


    text_inputer(browser.find_element_by_xpath("//input[@placeholder='Input your first name']"))
    text_inputer(browser.find_element_by_xpath("//input[@placeholder='Input your last name']"))
    text_inputer(browser.find_element_by_xpath("//input[@placeholder='Input your email']"))

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
