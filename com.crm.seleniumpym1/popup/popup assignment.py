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
parent=driver.current_window_handle
driver.find_element(By.XPATH,"//input").click()
sleep(2)
childs=driver.window_handles
for child in childs:
    driver.switch_to.window(child)
    sleep(1)
    if childs[0]!=child:
        driver.maximize_window()
        actual_url = driver.current_url

driver.switch_to.window(parent)
sleep(2)
driver.close()