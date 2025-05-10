
from selenium import webdriver
#initial steps to avoid the closing the browser
options=webdriver.ChromeOptions()
# options=webdriver.EdgeOptions()
options.add_experimental_option("detach",True)
#open the browser
webdriver.Chrome(options=options)
# webdriver.Edge(options=options)
