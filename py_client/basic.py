import requests

endpoint = 'http://localhost:8000/api'
endpoint_two = 'http://localhost:8000/api/model'
endpoint_three = 'http://localhost:8000/api/drf_intro'

# get_response = requests.get(endpoint, json={'name' : 'kaiel'}, params={'abc' : '123'})

# this is for the get request
# get_response = requests.get(endpoint_three)

# this is for the post request
responses = requests.post(endpoint_three, json={"name" : 'gabe'})

print(responses.json())