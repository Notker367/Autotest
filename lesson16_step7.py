from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/huge_form.html"

try:
    browser = webdriver.Chrome(executable_path="C:\webdrivers\chromedriver_win32\chromedriver_win32 (1)\chromedriver.exe")
    browser.get(link)

    elements = browser.find_elements_by_tag_name("input")
    n = 0
    for element in elements:
        n = n + 1
        element.send_keys("Мой ответ" + str(n))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла