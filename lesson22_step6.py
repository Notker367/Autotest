from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/execute_script.html"

def calc(x):
    return str(math.log((abs(12 * math.sin(int(x))))))


try:
    browser = webdriver.Chrome(executable_path="C:\webdrivers\chromedriver_win32\chromedriver_win32 (1)\chromedriver.exe")
    browser.get(link)

    x_el = browser.find_element_by_id("input_value")
    x_str = x_el.text
    x_end_str = calc(x_str)

    pole_el = browser.find_element_by_tag_name("input")
    pole_el.send_keys(x_end_str)

    butt_el = browser.find_element_by_tag_name("button")
    browser.execute_script("return arguments[0].scrollIntoView();", butt_el)

    chbox_el = browser.find_element_by_id("robotCheckbox")
    chbox_el.click()

    radio_el = browser.find_element_by_id("robotsRule")
    radio_el.click()

    butt_el.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла