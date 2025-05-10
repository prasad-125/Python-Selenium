from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

from selenium.webdriver.common.devtools.v120.input_ import DragData

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demo.automationtesting.in/Register.html")
sleep(2)
driver.find_element(By.XPATH,"//input[@ng-model='FirstName']").send_keys("PRASAD")
driver.find_element(By.XPATH,"//input[@ng-model='LastName']").send_keys("HIREY")
driver.find_element(By.XPATH,"//textarea[@ng-model='Adress']").send_keys("Pune maharashtra")
driver.find_element(By.XPATH,"//input[@ng-model='EmailAdress']").send_keys("prasad123@gmail.com")
action=ActionChains(driver)
action.key_down(Keys.TAB).perform()
action.send_keys("7620591550").perform()
action.key_down(Keys.ENTER).perform()
driver.find_element(By.XPATH,"//input[@value='Male']").click()
hobbies = driver.find_elements(By.XPATH, "//div[@class='form-group'][6]/div/div/input")
for hobi in hobbies:
    hobi.click()

driver.find_element(By.ID,"msdd").click()
sleep(2)
driver.find_element(By.XPATH,"//a[text()='English']").click()
driver.find_element(By.XPATH,"//a[text()='Hindi']").click()
