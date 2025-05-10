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
    driver.find_element(By.CSS_SELECTOR,'.ico-register').click()
    # time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#gender-male').click()
    # time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#FirstName').send_keys("prasad")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#LastName').send_keys("hirey")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#Email').send_keys("hirayprasad10@gmail.com")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, '#Password').send_keys("12345678")
    driver.find_element(By.CSS_SELECTOR, '#ConfirmPassword').send_keys("12345678")
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, "input[value='Register']").click()

else:
    print("Im not in webpage")