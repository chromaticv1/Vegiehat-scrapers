from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome()


def clickingOnNotification(driver):
  dialog = driver.find_element(By.ID, "headlessui-dialog-:r0:")
  inner_elements = dialog.find_elements(By.TAG_NAME, "button")
  inner_elements[1].click() # Clicking on No 
  
