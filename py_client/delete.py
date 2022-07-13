import requests

product_id = input("Enter the product id you want to delete: ")

try:
    product_id = int(product_id)
except:
    product_id = None
    print(f'{product_id} is not valid')

if product_id:
    # import pdb;pdb.set_trace()
    endpoint = f"http://localhost:8000/api/products/{product_id}/delete/"

    get_response = requests.delete(endpoint) 

    print(get_response.status_code, get_response.status_code==204)
