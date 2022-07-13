import requests


endpoint = "http://localhost:8000/api/products/"

data = {
    'title':'This is from create MIXIN',
    'price':18.22
}

get_response = requests.post(endpoint, json=data) 

print(get_response.json())
