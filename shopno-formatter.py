import json
import os

raw_outputs = os.listdir("./raw_outputs")

# Open and read the JSON file

# Print the data
for jsonfile in raw_outputs:
    print(jsonfile)
    with open(f'./raw_outputs/{jsonfile}', 'r') as file:
        data = json.load(file)

    formatted_products = []

    for raw_product in data:
        price_per_unit = raw_product['raw_price'].replace('\n',' ').split(' ')[0][1:]
        product = {'id': raw_product['id'],
                   'name': raw_product['name'],
                   'price': price_per_unit,
                   'unit': raw_product['special_quantity'] if
                   'special_quantity' in raw_product else
                   raw_product['raw_price'].split(' ')[-1]
                   }
        print(product)
        formatted_products.append(product)
    with open(f"./outputs/{jsonfile}", "w") as f:
        f.write(json.dumps(formatted_products))
