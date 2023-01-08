from selenium import webdriver
from selenium.webdriver.common.by import By

__doc__ = """
    Go to saucedemo.com
    Login with standard_user and secret_sauce credentials
    
"""


def run_test(driver):
    # Go to saucedemo.com
    driver.get("https://www.saucedemo.com/")

    # Login with standard_user and secret_sauce credentials
    driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("standard_user")
    driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("secret_sauce")
    driver.find_element(By.XPATH, "//input[@data-test='login-button']").click()
    assert driver.find_element(By.XPATH, "//span[@class='title']").is_displayed(), True


try:
    driver = webdriver.Chrome(executable_path="C:\repos\SeleniumWithPython\chromedriver.exe")
    run_test(driver)
except Exception as e:
    print(f"Error occurred with exception: {e}")
