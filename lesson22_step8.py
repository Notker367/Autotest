from selenium import webdriver
import time
import math
import os

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome(executable_path="C:\webdrivers\chromedriver_win32\chromedriver_win32 (1)\chromedriver.exe")
    browser.get(link)

    f_name_el = browser.find_element_by_name("firstname")
    f_name_el.send_keys("First")

    l_name_el = browser.find_element_by_name("lastname")
    l_name_el.send_keys("Last")

    f_name_el = browser.find_element_by_name("email")
    f_name_el.send_keys("Email")

    att_file_el = browser.find_element_by_id("file")
    current_dir = os.path.abspath(os.path.dirname(__file__))     # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'HEllo.txt')           # добавляем к этому пути имя файла
    att_file_el.send_keys(file_path)

    butt_el = browser.find_element_by_class_name("btn.btn-primary")
    butt_el.click()



finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла