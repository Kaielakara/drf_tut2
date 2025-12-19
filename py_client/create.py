import requests

endpoint = 'http://localhost:8000/dropbox/create/'

data = [

]

post_res = requests.post(endpoint, json=data)

print(f"{post_res.json()}")