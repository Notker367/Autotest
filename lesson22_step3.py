from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

# link = "http://suninjuly.github.io/selects1.html"
link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome(executable_path="C:\webdrivers\chromedriver_win32\chromedriver_win32 (1)\chromedriver.exe")
    browser.get(link)

    x_el = browser.find_element_by_id("num1")
    x_str = x_el.text
    y_el = browser.find_element_by_id("num2")
    y_str = y_el.text
    summ = int(x_str) + int(y_str)
    print(1)

#    dd_list = Select(browser.find_element_by_id("dropdown"))
    ddlist = Select(browser.find_element_by_tag_name("select"))
    print(2)
    ddlist.select_by_value(str(summ))

    Submit_button = browser.find_element_by_tag_name("button")
    Submit_button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла