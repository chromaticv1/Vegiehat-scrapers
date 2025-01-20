from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 
import pandas as pd
import re

driver = webdriver.Chrome()
# Product Information
productList = [
  {
    "id": 1,
    "name": 'Rice',
    "altName": ["Rice", "Chal"],
    "unit": 'kg',
    "shwapno": {
        "Loose": "https://www.shwapno.com/loose-rice",
        "Packet": "https://www.shwapno.com/packed-rice"
      }
  },
  {
    "id": 2,
    "name": 'Flour',
    "altName": ["Flour", "Maida", "Atta"],
    "unit": 'kg',
    "shwapno": "https://www.shwapno.com/flours"
  },
  {
    "id": 3,
    "name": 'Lentil',
    "altName": ["Lentil", "Dal"],
    "unit": 'kg',
    "shwapno": {
      "Loose": "https://www.shwapno.com/loose-daal",
      "Packet": "https://www.shwapno.com/packed-daal"
    }
  },
  {
    "id": 4,
    "name": "Soybean Oil",
    "altName": ["Soybean Oil", "Soyabean Oil"],
    "unit": 'liter',
    "shwapno": "https://www.shwapno.com/soybean-oil",
  },
  {
    "id": 5,
    "name": "Salt",
    "altName": ["Salt"],
    "unit": 'kg',
    "shwapno": "https://www.shwapno.com/salt"
  },
  {
    "id": 6,
    "name": "Sugar",
    "altName": ["Sugar", "Chini"],
    "unit": 'kg',
    "shwapno": "https://www.shwapno.com/sugar"
  },
  {
    "id": 7,
    "name": "Egg",
    "altName": ["Egg"],
    "unit": '4 pieces',
    "shwapno": "https://www.shwapno.com/eggs"
  },
  {
    "id": 8,
    "name": "Chicken",
    "altName": ["Chicken"],
    "unit": 'kg',
    "shwapno": "https://www.shwapno.com/chicken"
  },
  {
    "id": 9,
    "name": "Potato",
    "altName": ["Potato", "Alu"],
    "unit": 'kg',
    "shwapno": "https://www.shwapno.com/dry-vegetables"
  },
  {
    "id": 10,
    "name": "Eggplant",
    "unit": 'kg',
    "shwapno": []
  },
  {
    "id": 11,
    "name": "Onion",
    "altName": ["Onion", "Piyaj"],
    "unit": 'kg',
    "shwapno": "https://www.shwapno.com/dry-vegetables",
    "categories": ["Deshi", "Indian", "Pakisthani", "Other"],
  }, 
  {
    "id": 12,
    "name": "Green Chilli",
    "unit": 'kg',
    "shwapno": []
  }
]

def adjust_price_by_quantity(name, price):
  # Check for kg and divide price by the quantity
  kg_match = re.search(r'(\d+(\.\d+)?)\s?kg', name, re.IGNORECASE)
  if kg_match:
    quantity = float(kg_match.group(1))
    return round(price / quantity, 2)
  
  # Check for gm and adjust price for 1kg equivalent
  gm_match = re.search(r'(\d+)\s?gm', name, re.IGNORECASE)
  if gm_match:
    quantity = int(gm_match.group(1))
    if quantity > 0:
      return round(price * (1000 / quantity), 2)
  
  # Check for liters (L) and divide price by the quantity
  l_match = re.search(r'(\d+(\.\d+)?)\s?L', name, re.IGNORECASE)
  if l_match:
    quantity = float(l_match.group(1))
    return round(price / quantity, 2)
  
  # Check for ml and adjust price for 1L equivalent
  ml_match = re.search(r'(\d+)\s?ml', name, re.IGNORECASE)
  if ml_match:
    quantity = int(ml_match.group(1))
    if quantity > 0:
      return round(price * (1000 / quantity), 2)
  
  # Return the original price if no patterns match
  return price



# Get Data Function
def get_data(driver, link, category, sub_category, altNames, unit):
  try:
    driver.get(link)
    time.sleep(5)
    main = driver.find_element(By.CSS_SELECTOR, "#product-grid")
    products = main.find_elements(By.CSS_SELECTOR, "div.product-box div.product-box-info")
    for product in products:
      name = product.find_element(By.CSS_SELECTOR, "h2 > a").text
      for altName in altNames:
        if altName.lower() in name.lower():
          price = product.find_element(By.CSS_SELECTOR, "div.product-price > span.active-price").text
          price = float(price.split('৳')[1])
          price = adjust_price_by_quantity(name, price)
          newList.append({"id": len(newList)+1 , "Name": name, "Price": price, "Unit": unit, "category": category, "sub_category": sub_category})
      else: # This in for for loop
        print(name) # to see all the names
  except Exception as e:
    print(f"Error fetching data: {e}") 

# Starting Code
URL = "https://www.shwapno.com/"
driver.get(URL)
time.sleep(5)

# Notifications
noBtn = driver.find_element(By.CSS_SELECTOR, "#headlessui-dialog-panel-\:r1\: > div.mt-3.border-t.pt-3.text-center > button.mx-2.inline-flex.justify-center.rounded-full.border-0.bg-darkLight.px-6.py-2.text-sm.font-medium.leading-none.text-black.outline-none.hover\:bg-darkLight")
noBtn.click()
time.sleep(0.5)

newList = []

# Search and Select Product
for product in productList:
  if (isinstance(product["shwapno"], str)):
    get_data(driver, product["shwapno"], product["name"], "", product["altName"], product["unit"])
    time.sleep(1)
  elif (isinstance(product["shwapno"], dict)):
    get_data(driver, product["shwapno"]["Loose"], product["name"], "Loose", product["altName"], product["unit"]) 
    time.sleep(1)
    get_data(driver, product["shwapno"]["Packet"], product["name"], "Packet", product["altName"], product["unit"])

df = pd.DataFrame(newList) 
df.to_csv('product_data.csv', index=False) 
print(df)
time.sleep(5)
driver.quit()