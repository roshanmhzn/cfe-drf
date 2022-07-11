import requests

endpoint = "http://httpbin.org/status/200"
# endpoint = "http://httpbin.org/anything"

get_response = requests.get(endpoint, json={"query":"hello world"}) #Application Programming Interface
# print(get_response.text)

# HTTP Requests -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Notation ~ Python Dict

print(get_response.status_code)