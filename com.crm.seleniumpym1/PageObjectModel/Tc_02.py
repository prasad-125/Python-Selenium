import time
from selenium import webdriver
from PageObjectModel.HomePage import Admin
from PageObjectModel.LoginPage import Login

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
driver=webdriver.Chrome(options=options)
expected_url="https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"
driver.maximize_window()
driver.implicitly_wait(15)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")



