from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

from functions.shwapno_2 import clickingOnNotification, searchItems

driver = webdriver.Chrome()

shwapno = "https://www.shwapno.com/"
driver.get(shwapno)
time.sleep(1)

# Notifications
clickingOnNotification(driver)

productList = ["Rice", "Flour", "Lentil", "Soybean Oil", "Salt", "Egg", "Chicken", "Potato", "Eggplant","Onion", "Green Chilli"]


for item in productList:
  main = driver.find_element(By.TAG_NAME, "body")
  searchItems(main, item)




time.sleep(10)