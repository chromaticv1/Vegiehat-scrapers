from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

web = 'https://www.shwapno.com/eggs'
path = './chromedriver-win64/chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)


driver.get(web)

time.sleep(.5)
notification = driver.find_element(By.CSS_SELECTOR, "#headlessui-dialog-panel-\:r1\: > div.mt-3.border-t.pt-3.text-center > button.mx-2.inline-flex.justify-center.rounded-full.border-0.bg-darkLight.px-6.py-2.text-sm.font-medium.leading-none.text-black.outline-none.hover\:bg-darkLight")
notification.click()
time.sleep(.2)
products = driver.find_elements(By.CSS_SELECTOR, "div.product-box div.product-box-info")
for product in products:
    title = product.find_element(By.CSS_SELECTOR, "h2").text
    price = product.find_element(By.CSS_SELECTOR, ".active-price").text
    print(title, price)

driver.quit()