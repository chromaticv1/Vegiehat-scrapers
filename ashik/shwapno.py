from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 
import csv

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
# productList = ["Rice", "Eggplant"]

def get_data(categoryName, startingIndex):
  # Search for products
  search_box = driver.find_element(By.CSS_SELECTOR, "#search-input")
  search_box.clear()
  search_box.send_keys(categoryName)
  search_box.send_keys(Keys.ENTER)

  time.sleep(10)

  try:
    main = driver.find_element(By.CSS_SELECTOR, "#product-grid")
    products = main.find_elements(By.CSS_SELECTOR, "div.product-box div.product-box-info")


    for product in products:
      name = product.find_element(By.CSS_SELECTOR, "h2 > a").text
      price = product.find_element(By.CSS_SELECTOR, "div.product-price > span.active-price").text
      price = price.split('৳')[1]
      unit = product.find_element(By.CSS_SELECTOR, "div.product-price > span.font-normal.self-end").text
      product_data = {"id": startingIndex, "name": name, "category": categoryName, "price": price, "unit": unit}
      data.append(product_data)
      print(name, price, unit)
      startingIndex += 1
  except Exception as e:
        print(f"Error fetching data for category {categoryName}: {e}")    


for category in productList:
  get_data(category, len(data)+1)
  time.sleep(5)
  
print(data)  
field_names = ["id", "name", "category", "price", "unit"]
with open('Data.csv', 'w') as csvfile: 
    writer = csv.DictWriter(csvfile, fieldnames = field_names) 
    writer.writeheader() 
    writer.writerows(data) 