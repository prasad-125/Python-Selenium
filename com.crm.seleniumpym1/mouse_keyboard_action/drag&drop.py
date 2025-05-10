from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from time import sleep

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
sleep(2)
act=ActionChains(driver)
source1=driver.find_element(By.ID,"box6")
target1=driver.find_element(By.ID,"box106")
# act.drag_and_drop(source1,target1).perform()
source2=driver.find_element(By.ID,"box7")
target2=driver.find_element(By.ID,"box107")
# act.drag_and_drop(source2,target2).perform()

#click and hold --------->
# act.click_and_hold(source1).release(target1).perform()

# drag_and_drop_by_offset --------->
act.drag_and_drop_by_offset(source1,508,501).perform()