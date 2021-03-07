import pytest
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome(executable_path=r"D:\WebDrvers\Chrome\chromedriver_win32\chromedriver.exe")
    yield browser
    print("\nquit browser..")
    browser.quit()
