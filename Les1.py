from selenium import webdriver

driver = webdriver.Firefox(executable_path="C:\webdrivers\geckodriver-v0.27.0-win64\geckodriver.exe")
driver.get("http://yahoo.com")

driver = webdriver.Chrome(executable_path="C:\webdrivers\chromedriver_win32\chromedriver_win32 (1)\chromedriver.exe")
driver.get("http://yahoo.com")