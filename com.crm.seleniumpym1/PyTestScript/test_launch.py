from selenium import webdriver

def test_dws():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://demowebshop.tricentis.com/")
    print("demo workshop")
def test_rcb():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://royalchallengers.com/")
    print("no cup")
def test_csk():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://www.chennaisuperkings.com/")
    print("chennai mai 6")
def test_mi():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://www.mumbaiindians.com/")
    print("mumbai cha raja")










