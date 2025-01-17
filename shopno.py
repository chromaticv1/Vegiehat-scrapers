from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import json
data = {"id":[], "product_name":[], "product_keyword":[], "loose":[], "price":[], }
url_domain = 'https://www.shwapno.com/'
url_subs = [
    'dry-vegetables',
     'eggs'
    ]

path = './chromedriver-win64/chromedriver.exe'
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
service = Service(executable_path=path)
driver = webdriver.Chrome(service=service, options=options)


def scrape(catagory,should_remove_notification=False):
    product_dataset = []
    time.sleep(1)
    if should_remove_notification:
        notification = driver.find_element(By.CSS_SELECTOR,
                                           "#headlessui-dialog-panel-\:r1\: > div.mt-3.border-t.pt-3.text-center > button.mx-2.inline-flex.justify-center.rounded-full.border-0.bg-darkLight.px-6.py-2.text-sm.font-medium.leading-none.text-black.outline-none.hover\:bg-darkLight")
        notification.click()
        time.sleep(.5)

    products = driver.find_elements(By.CSS_SELECTOR, "div.product-box div.product-box-info")
    i = 0
    for product  in products:
        product_data = {'id': i,
                        'name': product.find_element(By.CSS_SELECTOR, "h2").text,
                        'raw_price': product.find_element(By.CSS_SELECTOR, ".product-price").text}
        if 'Unit' in product_data['raw_price']:
            product_data['special_quantity'] = product.find_element(By.CSS_SELECTOR, "div.product-box-info div.product-box-attribute").text.split('\n')[0]

        product_dataset.append(product_data)
        i += 1
    with open(f"raw_outputs/shopno-{catagory}.json", "w") as f:
        f.write(json.dumps(product_dataset))


for i, url_sub in enumerate(url_subs):
    url = url_domain + url_sub
    driver.get(url)
    if i == 0:
        scrape(url_sub,True)
    else:
        scrape(url_sub)
    time.sleep(1.5)
driver.quit()
