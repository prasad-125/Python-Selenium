from selenium import webdriver
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
from datetime import datetime
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://demowebshop.tricentis.com/")
sleep(2)
date=datetime.now()
print(date)          # 2025-04-03 15:56:21.580015  -----> replace the : to convert to str
s=str(date).replace(":","-")
driver.save_screenshot("C:\\Users\\Lenovo\\Desktop\\ScreenShot\\dws"+s+".png")
