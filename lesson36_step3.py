import pytest
from selenium import webdriver
import time
import math
import unittest

links = [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1",
    "https://stepik.org/lesson/236896/step/1"
]



@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(executable_path=r"D:\WebDrvers\Chrome\chromedriver_win32\chromedriver.exe")
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize("link", links)
class TestText():
    def test_input_text(self, browser, link):
        # открываем ссылку
        browser.get(link)
        browser.implicitly_wait(10)
        # нахожу поле, ввожу текст
        textzone = browser.find_element_by_tag_name("textarea")
        answer = math.log(int(time.time()))
        textzone.send_keys(str(answer))
        #print(str(math.log(int(time.time()))))
        # нахожу кнопку и кликаю
        #time.sleep(5)
        button = browser.find_element_by_css_selector("button.submit-submission")
        #print(str(button))
        button.click()
        #print("im click")
        #time.sleep(2)
        # нахожу текст, записываю
        mytext = browser.find_element_by_class_name("smart-hints__hint")
        #print(mytext.text)
        assert mytext.text == "Correct!"



if __name__ == "__main__":
    unittest.main()
