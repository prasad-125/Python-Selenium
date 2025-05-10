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
driver.find_element(By.XPATH,"//a[@href='/25-virtual-gift-card']").click()
sleep(2)
driver.find_element(By.XPATH,"//input[@class='recipient-name']").send_keys("janu")
sleep(2)
driver.find_element(By.XPATH,"//input[@id='giftcard_2_RecipientEmail']").send_keys("janu12@gmail.com")
sleep(2)
driver.find_element(By.XPATH,"//input[@id='giftcard_2_SenderName']").send_keys("prasad")
sleep(2)
driver.find_element(By.XPATH,"//input[@id='giftcard_2_SenderEmail']").send_keys("parshu12@gmail.com")
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
driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
sleep(2)
driver.find_element(By.XPATH,"//input[@value='Update shopping cart']").click()