from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://demoapps.qspiders.com/ui?scenario=1")
sleep(2)
driver.find_element(By.XPATH,"//li[text()='Disabled']")