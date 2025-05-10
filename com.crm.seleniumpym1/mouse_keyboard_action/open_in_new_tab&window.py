from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
sleep(2)
action=ActionChains(driver)
books=driver.find_element(By.XPATH,"//a[contains(text(),'Books')]")
# open in new tab -------->      ctrl+click
action.key_down(Keys.CONTROL).click(books).perform()
action.key_up(Keys.CONTROL).perform()
sleep(2)
# open in new window ------->    shift+click
computer=driver.find_element(By.XPATH,"//a[contains(text(),'Computers')]")
action.key_down(Keys.SHIFT).click(computer).perform()