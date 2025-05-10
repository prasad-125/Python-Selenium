from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
sleep(2)
parent=driver.current_window_handle
print(parent)
print(type(parent))
action=ActionChains(driver)
action.key_down(Keys.PAGE_DOWN).perform()
sleep(2)
driver.find_element(By.XPATH,"//a[text()='Facebook']").click()
sleep(2)
child=driver.window_handles
driver._switch_to.window(child[1])
sleep(2)
driver.find_element(By.XPATH,"//span[text()='Create new account']").click()
sleep(2)
driver.get("https://demowebshop.tricentis.com/")
sleep(2)
driver.find_element(By.XPATH,"//a[text()='Twitter']").click()
