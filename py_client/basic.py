import requests

# endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api/" #http://127.0.0.1:8000/ 

# res = requests.get(endpoint)
# print(res.text)
# print(res.status_code)

# res = requests.get(endpoint,json={'test':'hello world'})
# print(res.text)

# res = requests.get(endpoint,data={'test':'hello world'})
# # print(res.text)
# print(res.json())


# get_response = requests.post(endpoint, json={"title": "Abc123", "content": "Hello world", "price": "abc134"}) # HTTP Request
get_response = requests.get(endpoint,params={'product_id':123}, json={"title": "Abc123", "content": "Hello world", "price": "abc134"})
# print(get_response.headers)
print(get_response.text) # print raw text response
# print(get_response.status_code)

# HTTP Request -> HTML
# REST API HTTP Request -> JSON
# JavaScript Object Nototion ~ Python Dict
# print(res.json()['message'])
# print(get_response.status_code)