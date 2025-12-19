import json
import requests
from getpass import getpass

# endpoint='http://localhost:8000/api/list'

# post_res = requests.get(endpoint)

endpoint = 'http://localhost:8000/dropbox/api-token-auth/'
user = input("What is your name \n")
password = getpass("What is your password \n")

auth_post = requests.post(endpoint, json={'username' : user, 'password' : password})

if auth_post.status_code == 200:
    token = auth_post.json()['token']
    headers = {
        'Authorization' : f"Bearer {token}"
    }

    pk = input("What's the id of the content you want to look at? \n")

    endpoint_two = f'http://localhost:8000/dropbox/{pk}'

    get_res = requests.get(endpoint_two, headers=headers)

    print(json.dumps(get_res.json(), indent = 4))

else:
    print("Wrong Username/Password")