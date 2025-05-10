import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
expected_url = "https://demowebshop.tricentis.com/"
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
actual_url = driver.current_url
if actual_url == expected_url:
    print("Im in DWS Webpage")
    driver.find_element(By.ID, "small-searchterms").send_keys("laptop")
    time.sleep(2)
    #by using linktext---->
    # driver.find_element(By.CLASS_NAME,"button-1 ").click()
    #by using css selector----->
    # driver.find_element(By.CSS_SELECTOR,"input[value='Search']").click()
    driver.find_element(By.CSS_SELECTOR,'.button-1.search-box-button').click()
