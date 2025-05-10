from selenium import webdriver
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://demoapps.qspiders.com/ui?scenario=1")
driver.find_element(By.XPATH,"//section[text()='Popups']").click()
driver.find_element(By.XPATH,"//section[text()='Browser Windows']").click()
driver.find_element(By.ID,"browserLink1").click()
act=driver.window_handles
driver.switch_to.window(act[1])

driver.find_element(By.ID,"email").send_keys("prasad@123.com")
driver.find_element(By.ID,"password").send_keys("1234")
driver.find_element(By.ID,"confirm-password").send_keys("1234")