from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

# popup notification popup block ---------->

# options = webdriver.ChromeOptions()
# options.add_experimental_option("detach", True)
# options.add_argument("--disable-notifications")             #used to avoid the notification popup
# driver = webdriver.Chrome(options=options)
# driver.maximize_window()
# driver.get("https://www.easemytrip.com/")
# sleep(2)


# qspider authentiction popup login automatic by adding username and pass in https link --------->

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://admin:admin@basic-auth-git-main-shashis-projects-4fa03ca5.vercel.app/")    # add username =admin pass=admin@
sleep(2)
