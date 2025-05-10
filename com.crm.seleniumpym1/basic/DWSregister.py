from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
expected_url = "https://demowebshop.tricentis.com/"
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
actual_url = driver.current_url

if actual_url == expected_url:
    print("Im in DWS Webpage")
    driver.find_element(By.CLASS_NAME, "ico-register").click()
    time.sleep(1)
    driver.find_element(By.ID, "gender-male").click()
    time.sleep(1)
    driver.find_element(By.ID, "FirstName").send_keys("prasad")
    time.sleep(1)
    driver.find_element(By.ID, "LastName").send_keys("hirey")
    time.sleep(1)
    driver.find_element(By.ID, "Email").send_keys("hirayprasad1@gmail.com")
    time.sleep(1)
    driver.find_element(By.ID, "Password").send_keys("12345678")
    driver.find_element(By.ID, "ConfirmPassword").send_keys("12345678")
    time.sleep(1)
    driver.find_element(By.ID, "register-button").click()

else:
    print("Im not in webpage")