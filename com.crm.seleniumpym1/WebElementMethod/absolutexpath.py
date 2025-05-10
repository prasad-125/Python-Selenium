from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
expected_url = "https://demowebshop.tricentis.com/"
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[4]/div/div/div[2]/div/ul/li/a").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[4]/div/div[4]/div[2]/form/div/div/div[2]/div[2]/div/div/input").click()
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[4]/div/div[4]/div[2]/form/div/div/div[2]/div[2]/div[2]/input").send_keys("prasad")
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[4]/div/div[4]/div[2]/form/div/div/div[2]/div[2]/div[3]/input").send_keys("hirey")
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[4]/div/div[4]/div[2]/form/div/div/div[2]/div[2]/div[4]/input").send_keys("hirey@gmail.com")
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[4]/div/div[4]/div[2]/form/div/div/div[3]/div[2]/div/input").send_keys("12345678")
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[4]/div/div[4]/div[2]/form/div/div/div[3]/div[2]/div[2]/input").send_keys("12345678")
time.sleep(2)
driver.find_element(By.XPATH,"/html/body/div[4]/div/div[4]/div[2]/form/div/div/div[4]/input").click()
