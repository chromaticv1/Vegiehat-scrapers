from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

from functions.shwapno_2 import clickingOnNotification

driver = webdriver.Chrome()

shwapno = "https://www.shwapno.com/"
driver.get(shwapno)
time.sleep(1)

# Notifications
clickingOnNotification(driver)

productList = ["Rice", ""]


# search_box = driver.find_element(By.CSS_SELECTOR, ".gLFyf")
# search_box.send_keys("shwapno")
# search_box.send_keys(Keys .ENTER)

time.sleep(10)