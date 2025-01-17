from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 



def clickingOnNotification(driver):
  dialog = driver.find_element(By.ID, "headlessui-dialog-:r0:")
  inner_elements = dialog.find_elements(By.TAG_NAME, "button")
  inner_elements[1].click() # Clicking on No 
  

def searchItems(parent, itemName):
  search_box = parent.find_element(By.CSS_SELECTOR, "#search-input")
  search_box.clear()
  search_box.send_keys(itemName)
  search_box.send_keys(Keys.ENTER)
  time.sleep(15)