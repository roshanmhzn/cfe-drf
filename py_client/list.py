import requests
from getpass import getpass


auth_endpoint = "http://localhost:8000/api/auth/"
username = input("What's your username? ")
password = getpass("What's your password? ")

auth_response = requests.post(auth_endpoint, json={'username': username, 'password':password}) 

print(auth_response.json())

if auth_response.status_code == 200:
    token = auth_response.json()['token']
    headers = {
        'Authorization': f"Bearer {token}"
    } 
    endpoint = "http://localhost:8000/api/products/"

    get_response = requests.get(endpoint, headers=headers) 

    print(get_response.json())
