
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

@pytest.fixture
def setup():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.implicitly_wait(15)
    yield
    driver.quit()



