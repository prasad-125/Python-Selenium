from selenium import webdriver
options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)
#OPEN THE BROWSER
driver=webdriver.Chrome(options=options)
#MAXIMIZE THE BROWSER
driver.maximize_window()
#ENTER INTO DWS HOMEPAGE
driver.get("https://demowebshop.tricentis.com/")
#CLOSE BROWSER
driver.close()