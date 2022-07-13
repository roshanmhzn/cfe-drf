import requests

# endpoint = "http://httpbin.org/status/200"
# endpoint = "http://httpbin.org/anything"
# endpoint = "http://localhost:8000/" # http://127.0.0.1:8000/
endpoint = "http://localhost:8000/api/" # http://127.0.0.1:8000/api/

get_response = requests.post(endpoint, params={'abc':123}, json={'title': "ABC123", 
                                                                "content":"Voldemort",
                                                                'price':'15.00'}) 

# HTTP Requests -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Notation ~ Python Dict

# print(get_response.headers)
# print(get_response.text)
# print(get_response.status_code)
print(get_response.json())
