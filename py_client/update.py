import requests

endpoint = 'http://localhost:8000/product/3/update'

data = {
    "name": "Vintage Denim Jacket",
    "description": "Classic blue denim jacket with copper buttons and a relaxed fit.",
    "price": "72.00",
    "category": "FC"
}

data_patch = {
    "price": "72.00",
}

put_res = requests.patch(endpoint, json=data_patch)

print(put_res.json())