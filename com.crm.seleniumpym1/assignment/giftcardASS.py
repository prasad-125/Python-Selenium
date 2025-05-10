import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
expected_url="https://demowebshop.tricentis.com/"
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://demowebshop.tricentis.com/")
time.sleep(2)
actual_url=driver.current_url
driver.find_element(By.CLASS_NAME,"ico-login").click()
driver.find_element(By.ID,"Email").send_keys("prasad00@gmail.com")
sleep(1)
driver.find_element(By.ID,"Password").send_keys("123456")
sleep(1)
driver.find_element(By.XPATH,"//input[@class='button-1 login-button']").click()
sleep(1)
driver.find_element(By.XPATH,"//div[@class='header-logo']").click()
sleep(1)
driver.find_element(By.XPATH,"//input[@class='button-2 product-box-add-to-cart-button']").click()
driver.find_element(By.XPATH,"//input[@class='recipient-name']").send_keys("janu")
sleep(1)
driver.find_element(By.XPATH,"//input[@id='giftcard_2_RecipientEmail']").send_keys("janu12@gmail.com")
sleep(2)
driver.find_element(By.XPATH,"//textarea[@class='message']").send_keys("hii ")
sleep(2)
quantity_input=driver.find_element(By.XPATH,"//input[@class='qty-input']")
current_quantity = int(quantity_input.get_attribute('value'))  # Get the current quantity
if current_quantity == 1:
    # Clear the current value and set the new value to 2
    quantity_input.clear()  # Clear the input field
    quantity_input.send_keys('2')  # Set the quantity to 2
sleep(2)
driver.find_element(By.XPATH,"//input[@id='add-to-cart-button-2']").click()
sleep(2)
driver.find_element(By.XPATH,"//a[text()='Shopping cart']").click()
sleep(2)
driver.find_element(By.CLASS_NAME,"ico-logout").click()
sleep(1)
driver.close()