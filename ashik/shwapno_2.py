from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time 


driver = webdriver.Chrome()
# Product Information
productList = [
  {
    "id": 1,
    "name": 'Rice',
    "unit": 'kg',
    "shwapno": {
        "Loose": "https://www.shwapno.com/loose-rice",
        "Packet": "https://www.shwapno.com/packed-rice"
      }
  },
  {
    "id": 2,
    "name": 'Flour',
    "unit": 'kg',
    "shwapno": "https://www.shwapno.com/flours"
  },
  {
    "id": 3,
    "name": 'Lentil',
    "unit": 'kg',
    "shwapno": {
      "Loose": "https://www.shwapno.com/loose-daal",
      "Packet": "https://www.shwapno.com/packed-daal"
    }
  },
  {
    "id": 4,
    "name": "Soybean Oil",
    "unit": 'liter',
    "shwapno": "https://www.shwapno.com/soybean-oil",
  },
  {
    "id": 5,
    "name": "Salt",
    "unit": 'kg',
    "shwapno": "https://www.shwapno.com/salt"
  },
  {
    "id": 6,
    "name": "Sugar",
    "unit": 'kg',
    "shwapno": "https://www.shwapno.com/sugar"
  },
  {
    "id": 7,
    "name": "Egg",
    "unit": '4 pieces',
    "shwapno": "https://www.shwapno.com/eggs"
  },
  {
    "id": 8,
    "name": "Chicken",
    "unit": 'kg',
    "shwapno": "https://www.shwapno.com/chicken"
  },
  {
    "id": 9,
    "name": "Potato",
    "unit": 'kg',
    "shwapno": "https://www.shwapno.com/dry-vegetables"
  },
  {
    "id": 10,
    "name": "Eggplant",
    "unit": 'kg',
    "shwapno": ""
  },
  {
    "id": 11,
    "name": "Onion",
    "unit": 'kg',
    "shwapno": "https://www.shwapno.com/dry-vegetables",
    "categories": ["Deshi", "Indian", "Pakisthani", "Other"],
  }, 
  {
    "id": 12,
    "name": "Green Chilli",
    "unit": 'kg',
    "shwapno": ""
  }
]


# Find Details
# def get_details():


# Get Data Function
def get_data(driver, link):
  try:
    driver.get(link)
    time.sleep(5)
    main = driver.find_element(By.CSS_SELECTOR, "#product-grid")
    products = main.find_elements(By.CSS_SELECTOR, "div.product-box div.product-box-info")
    for product in products:
      name = product.find_element(By.CSS_SELECTOR, "h2 > a").text
      price = product.find_element(By.CSS_SELECTOR, "div.product-price > span.active-price").text
      price = price.split('৳')[1]
      return [name, price]
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

# Search and Select Product
for product in productList:
  if (isinstance(product["shwapno"], str)):
    get_data(driver, product["shwapno"])
    time.sleep(1)
  elif (isinstance(product["shwapno"], dict)):
    get_data(driver, product["shwapno"]["Loose"])  
    time.sleep(1)
    get_data(driver, product["shwapno"]["Packet"])
time.sleep(50)
