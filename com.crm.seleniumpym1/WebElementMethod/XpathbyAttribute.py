from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
expected_url = "https://demowebshop.tricentis.com/"
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
sleep(2)
driver.find_element(By.ID,"small-searchterms").send_keys("computer")
sleep(2)
#xpath by attribute
driver.find_element(By.XPATH,"//input[@class='button-1 search-box-button']").click()
sleep(2)
#xpath by text function
driver.find_element(By.XPATH,"//a[text()='Register']").click()
# register=driver.find_element(By.XPATH,"//a[text()='Register']")
# data=register.text
# print(data)

#xpath by group of index
driver.find_element(By.XPATH,"(//input[@type='text'])[2]").send_keys("prasad")

