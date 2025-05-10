from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("file:///C:/Users/Lenovo/AppData/Local/Microsoft/Windows/INetCache/IE/JZ1OVPN6/MultipleWindow%20(1)[2].html")
sleep(2)
olive_url="https://www.olivegarden.com/home"
parent=driver.current_window_handle
driver.find_element(By.XPATH,"//input").click()
sleep(2)
handles=driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
    if olive_url==driver.current_url:
        driver.maximize_window()
        driver.back()
    else:
        driver.close()

