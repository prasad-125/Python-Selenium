from selenium import webdriver
def test_csk():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://www.chennaisuperkings.com/")

def test_mi():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://www.mumbaiindians.com/")