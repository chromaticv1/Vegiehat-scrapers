from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 

driver = webdriver.Chrome()

URL = "https://www.shwapno.com/"
driver.get(URL)
time.sleep(5)

# Notifications
dialog = driver.find_element(By.ID, "headlessui-dialog-:r0:")
inner_elements = dialog.find_elements(By.TAG_NAME, "button")
inner_elements[1].click() # Clicking on No

data = []
productList = ["Rice", "Flour", "Lentil", "Soybean Oil", "Salt", "Egg", "Chicken", "Potato", "Eggplant","Onion", "Green Chilli"]

def get_data(categoryName, startingIndex):
  # Search for products
  search_box = driver.find_element(By.CSS_SELECTOR, "#search-input")
  search_box.clear()
  search_box.send_keys(categoryName)
  search_box.send_keys(Keys.ENTER)

  time.sleep(10)


  main = driver.find_element(By.CSS_SELECTOR, "#product-grid")
  products = main.find_elements(By.CSS_SELECTOR, "div.product-box div.product-box-info")


  for product in products:
    name = product.find_element(By.CSS_SELECTOR, "h2 > a").text
    price = product.find_element(By.CSS_SELECTOR, "div.product-price > span.active-price").text
    unit = product.find_element(By.CSS_SELECTOR, "div.product-price > span.font-normal.self-end").text
    product_data = {"id": startingIndex, "name": name, "category": product, "price": price, "unit": unit}
    data.append(product_data)
    print(name, price, unit)
    startingIndex += 1


for category in productList:
  get_data(category, len(data)+1)
  time.sleep(5)
  
print(data)  