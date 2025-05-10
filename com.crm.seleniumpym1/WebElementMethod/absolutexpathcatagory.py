from time import sleep

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
driver.find_element(By.XPATH,"/html/body/div[4]/div/div[4]/div/div/div[2]/ul/li/a").click()
sleep(1)
driver.find_element(By.XPATH,"/html/body/div[4]/div/div[4]/div/div/div[2]/ul/li[2]/a").click()
sleep(1)
driver.find_element(By.XPATH,"/html/body/div[4]/div/div[4]/div/div/div[2]/ul/li[3]/a").click()
sleep(1)
driver.find_element(By.XPATH,"/html/body/div[4]/div/div[4]/div/div/div[2]/ul/li[4]/a").click()
sleep(1)
driver.find_element(By.XPATH,"/html/body/div[4]/div/div[4]/div/div/div[2]/ul/li[5]/a").click()
sleep(1)
driver.find_element(By.XPATH,"/html/body/div[4]/div/div[4]/div/div/div[2]/ul/li[6]/a").click()
sleep(1)
driver.find_element(By.XPATH,"/html/body/div[4]/div/div[4]/div/div/div[2]/ul/li[7]/a").click()
sleep(1)
driver.close()