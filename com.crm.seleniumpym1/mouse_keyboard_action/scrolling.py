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
act=ActionChains(driver)
#scroll down --->
act.key_down(Keys.ARROW_DOWN).perform()
#scroll down upto facebook ---->
# facebook=driver.find_element(By.XPATH,"//a[text()='Facebook']")
# act.scroll_to_element(facebook).perform()