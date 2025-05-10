from selenium import webdriver
def test_dws():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://demowebshop.tricentis.com/")

def test_rcb():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://royalchallengers.com/")