import requests


endpoint = "http://localhost:8000/api/products/2478320934"

get_response = requests.get(endpoint) 

print(get_response.json())
