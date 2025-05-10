from selenium import webdriver
from selenium.webdriver import ActionChains,Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
options.add_argument("--disable-notifications")
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.instagram.com/amchi_mumbai_indians/")
logo=driver.find_element(By.XPATH,"//img[@class='xpdipgo x972fbf xcfux6l x1qhh985 xm0m39n xk390pu x5yr21d xdj266r x11i5rnm xat24cr x1mh8g0r xl1xv1r xexx8yu x4uap5 x18d9i69 xkhd6sd x11njtxf xh8yej3']")
logo.screenshot("MILOGO.png")
driver.quit()