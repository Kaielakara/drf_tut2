import requests

endpoint = 'http://localhost:8000/api'

get_response = requests.get(endpoint, json={'name' : 'kaiel'}, params={'abc' : '123'})

print(get_response.json())