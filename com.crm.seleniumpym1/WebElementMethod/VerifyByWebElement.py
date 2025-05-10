#takw a webelement which is present only in home pagen
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
expected_url = "https://demowebshop.tricentis.com/"
driver = webdriver.Chrome(options=options)
driver.maximize_window()
time.sleep(2)
driver.get("https://demowebshop.tricentis.com/")
time.sleep(3)
vote=driver.find_element(By.ID,"vote-poll-1")
if vote.is_displayed():
    print("i am in dws page")
else:
    print("i am not in dws page")
driver.close()