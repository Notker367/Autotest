from selenium import webdriver
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

# говорим WebDriver искать каждый элемент в течение 5 секунд
# browser.implicitly_wait(5)

link = "http://suninjuly.github.io/explicit_wait2.html"

def calck(x):
    return str((math.log(abs(12*math.sin(int(x))))))

try:
    browser = webdriver.Chrome(executable_path="C:\webdrivers\chromedriver_win32\chromedriver_win32 (1)\chromedriver.exe")
    browser.get(link)

    butt_book_el = browser.find_element_by_id("book")
    nice_price = WebDriverWait(browser, 20).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    butt_book_el.click()

    x_el = browser.find_element_by_id("input_value")
    x_str = x_el.text
    x = calck(x_str)

    inp_el = browser.find_element_by_id("answer")
    inp_el.send_keys(x)

    butt_sub_el = browser.find_element_by_id("solve")
    butt_sub_el.click()

    aler_el = browser.switch_to.alert
    text_f_a = aler_el.text
    y = text_f_a.split(': ')[-1]
    print(y)


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

#Изменение для коммита
