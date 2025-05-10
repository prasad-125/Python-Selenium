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
barbeque_url="https://www.barbequenation.com/"
giallozafferano_url="https://www.giallozafferano.com/"
childs=driver.window_handles
for child in childs:
    driver.switch_to.window(child)
    if child!=childs[0]:
        driver.maximize_window()
        sleep(1)
        actual_url=driver.current_url
        if actual_url==barbeque_url:
            driver.find_element(By.XPATH,"//button[@id='hapiness-cart-btn']/following-sibling::button").click()
            sleep(1)

        elif actual_url==olive_url:
            driver.find_element(By.XPATH,"//div[@id='onetrust-close-btn-container']/button").click()

            sleep(2)
            driver.find_element(By.XPATH,"//a[text()='Log In']").click()
            sleep(2)
        elif actual_url == giallozafferano_url:
            sleep(1)
            driver.find_element(By.XPATH,"//div[@class='amecp_cookieBottom']/button").click()
            sleep(1)
            driver.find_element(By.XPATH,"//header[@id='gz-header']/div/span").click()
            sleep(2)

for child in childs:
    driver.switch_to.window(child)
    driver.close()
    sleep(1)
