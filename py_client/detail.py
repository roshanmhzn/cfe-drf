import requests


# endpoint = "http://localhost:8000/api/products/1"

# get_response = requests.get(endpoint) 

# print(get_response.json())



product_id = input("Enter the product id you want to use: ")

try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'{product_id} is not valid')


endpoint = f"http://localhost:8000/api/products/{product_id}/"

get_response = requests.get(endpoint) 

print(get_response.json())
