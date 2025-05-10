import time
from time import sleep
from selenium.webdriver import ActionChains,Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
expected_url="https://demowebshop.tricentis.com/"
driver=webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(20)
driver.get("https://demowebshop.tricentis.com/")
time.sleep(2)
actual_url=driver.current_url
sleep(2)
parent=driver.current_window_handle
expected_rss="https://demowebshop.tricentis.com/news/rss/1"
facebook_url="https://www.facebook.com/nopCommerce"
action=ActionChains(driver)
action.key_down(Keys.PAGE_DOWN).perform()
action.key_down(Keys.PAGE_DOWN).perform()
sleep(2)
apps=driver.find_elements(By.XPATH,"//div[@class='column follow-us']/ul/li/a")
for app in apps:
    actual_url1 = driver.current_url
    if expected_rss==actual_url1:
        driver.back()
    app.click()
    sleep(2)
childs=driver.window_handles
sleep(2)
for child in childs:
    driver.switch_to.window(child)
    actual_url2=driver.current_url
    if facebook_url == actual_url2:
        driver.find_element(By.XPATH, "//span[text()='Create new account']").click()
        sleep(2)
        driver.find_element(By.XPATH,"//input[@name='firstname']").send_keys("perl")
        sleep(1)
        driver.find_element(By.XPATH,"//input[@name='lastname']").send_keys("black")

















