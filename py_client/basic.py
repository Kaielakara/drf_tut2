import requests

endpoint = 'http://localhost:8000/api'
endpoint_two = 'http://localhost:8000/api/model'

# get_response = requests.get(endpoint, json={'name' : 'kaiel'}, params={'abc' : '123'})

get_response = requests.get(endpoint_two)

print(get_response.json())