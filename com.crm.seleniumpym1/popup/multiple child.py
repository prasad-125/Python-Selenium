from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
sleep(2)
parent=driver.current_window_handle
expected_rss="https://demowebshop.tricentis.com/news/rss/1"
twitter_url="https://x.com/nopCommerce"
facebook_url="https://www.facebook.com/nopCommerce"
youtube_url="https://www.youtube.com/user/nopCommerce"
sleep(2)
action=ActionChains(driver)
action.key_down(Keys.PAGE_DOWN).perform()
links=driver.find_elements(By.XPATH,"//div[@class='column follow-us']/ul/li/a")
for link in links:
    actual_url1=driver.current_url
    if expected_rss==actual_url1:
        driver.back()
    link.click()
    sleep(2)
childs=driver.window_handles
sleep(2)
for child in childs:
    driver.switch_to.window(child)
    actual_url2=driver.current_url
    if twitter_url==actual_url2:
        sleep(2)
        print("i am in twitter page")
        driver.find_element(By.XPATH,"//span[text()='Create account']").click()
    elif facebook_url==actual_url2:
        driver.find_element(By.XPATH,"//span[text()='Create new account']").click()
        sleep(2)
    elif youtube_url==actual_url2:
        driver.find_element(By.XPATH,"//input[@placeholder='Search']").send_keys("arjit sing song")
        action.key_down(Keys.ENTER).perform()
        sleep(1)

