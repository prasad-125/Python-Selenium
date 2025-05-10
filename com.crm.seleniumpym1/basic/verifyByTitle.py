import time

from selenium import webdriver
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
expected_title="Demo Web Shop"     #go to home page right click select inspect and copy title from head and paste here /to search the title press ctrl f
driver=webdriver.Chrome(options=options)
time.sleep(2)
driver.maximize_window()
driver.get("https://demowebshop.tricentis.com/")
time.sleep(2)
actual_title=driver.title
print(actual_title)
if expected_title==actual_title:
    print("i am in dws page")
else:
    print("i am not in dws page")

driver.close()
