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
#by using xpath by contains function
driver.find_element(By.XPATH,"//a[contains(text(),'Digital downloads')]").click()
album3rd=driver.find_element(By.XPATH,"//a[text()='3rd Album']/../following-sibling::div[3]/div/span")
print(album3rd.text)  #1.00
music=driver.find_element(By.XPATH,"//a[text()='Music 2']/../../div[3]/div/span")
print(music.text) # 10.00
music1=driver.find_element(By.XPATH,"(//a[text()='Music 2'])[2]/../../div[3]/div/span")
print(music1.text) # 3.00

