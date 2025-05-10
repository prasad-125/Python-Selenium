from selenium import webdriver
def test_hrm():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

def test_youtube():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://www.youtube.com/")
