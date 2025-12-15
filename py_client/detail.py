import requests

endpoint = 'http://localhost:8000/api/3'

post_res = requests.get(endpoint)

print(post_res.json())

