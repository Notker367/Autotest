from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"

def calck(x):
    return str((math.log(abs(12*math.sin(int(x))))))

try:
    browser = webdriver.Chrome(executable_path="C:\webdrivers\chromedriver_win32\chromedriver_win32 (1)\chromedriver.exe")
    browser.get(link)

    butt_want_el = browser.find_element_by_tag_name("button")
    butt_want_el.click()

    confrm_el = browser.switch_to.alert
    time.sleep(1)
    confrm_el.accept()

    x_el = browser.find_element_by_id("input_value")
    x_str = x_el.text
    x = calck(x_str)
    print(x)

    inp_el = browser.find_element_by_id("answer")
    inp_el.send_keys(x)

    butt_sub_el = browser.find_element_by_tag_name("button")
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