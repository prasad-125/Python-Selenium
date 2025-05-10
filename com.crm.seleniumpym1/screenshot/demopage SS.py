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
driver.get("https://demowebshop.tricentis.com/")
# driver.save_screenshot("dwshomepage.png")                                #webdriver
logo=driver.find_element(By.XPATH,"//div[@class='header-logo']")     #webelement
logo.screenshot("logo.png")
driver.quit()





