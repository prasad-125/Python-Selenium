import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
expected_url="https://demowebshop.tricentis.com/"
driver=webdriver.Chrome(options=options)
driver.maximize_window()
time.sleep(2)
driver.get("https://demowebshop.tricentis.com/")
time.sleep(2)
actual_url=driver.current_url

if expected_url==actual_url:
    print("I'm in DWS webpage")
    SearchField=driver.find_element(By.TAG_NAME,"input")
    SearchField.send_keys("prasad")
else:
    print("I'm not in DWS webpage")