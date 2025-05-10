import pytest
from selenium import webdriver
from selenium.webdriver.common.devtools.v85.log import clear


@pytest.mark.skip
def test_dws():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://demowebshop.tricentis.com/")
    print("demo workshop")
@pytest.mark.regression
def test_rcb():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://royalchallengers.com/")
    print("no cup")
@pytest.mark.function
def test_csk():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://www.chennaisuperkings.com/")
    print("chennai mai 6")
@pytest.mark.smoke
def test_mi():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(15)
    driver.get("https://www.mumbaiindians.com/")
    print("mumbai cha raja")








