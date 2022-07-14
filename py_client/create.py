import requests

headers = {
    'Authorization': 'Bearer 715138dc4a7e79249ec877147f3f6b8fc4e24b3a'
}

endpoint = "http://localhost:8000/api/products/"

data = {
    'title':'This is from TOKEN Creation Again',
    'price':18.22
}

get_response = requests.post(endpoint, json=data, headers=headers) 

print(get_response.json())
