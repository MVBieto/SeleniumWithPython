import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\repos\SeleniumWithPython\chromedriver.exe")
driver.get("https://www.saucedemo.com/")
driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("standard_user")
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("secret_sauce")
driver.find_element(By.XPATH, "//input[@data-test='login-button']").click()
time.sleep(5)
driver.close()

