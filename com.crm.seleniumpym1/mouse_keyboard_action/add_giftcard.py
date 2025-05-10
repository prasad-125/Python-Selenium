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
driver.find_element(By.XPATH,"//a[contains(text(),'Gift Cards')]").click()
cards=driver.find_elements(By.XPATH,"//div[@class='add-info']/div[2]/input")
card=0
for card in cards:
    card.click()
    sleep(2)
    count=driver.find_elements(By.XPATH,"//div[@class='giftcard']/div/input")
    # print(count)
    if len(count)==4:
        driver.find_element(By.XPATH, "//input[@id='giftcard_3_RecipientName']").send_keys("John Doe")
        sleep(2)
        driver.find_element(By.XPATH, "//input[@id='giftcard_1_RecipientEmail']").send_keys("recipient@example.com")
        sleep(2)
        driver.find_element(By.XPATH, "//input[@id='giftcard_3_SenderName']").send_keys("Your Name")
        sleep(2)
        driver.find_element(By.XPATH, "//input[@class='sender-email']").send_keys("your@example.com")
        sleep(2)
        driver.find_element(By.XPATH, "//textarea[@id='giftcard_3_Message']").send_keys("Happy Birthday!")
    else:
        driver.find_element(By.XPATH, "//input[@id='giftcard_3_RecipientName']").send_keys("John Doe")
        sleep(2)
        driver.find_element(By.NAME, "//input[@id='giftcard_3_SenderName']").send_keys("Your Name")
        sleep(2)
        driver.find_element(By.NAME, "//textarea[@id='giftcard_3_Message']").send_keys("Happy Birthday!")
















