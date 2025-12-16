import requests

try:
    id_key = int(input("Type in the id you want to delete: "))
except ValueError:
    print("Please input a Number")

else:
    endpoint = f'http://localhost:8000/product/{id_key}/delete'
    del_res = requests.delete(endpoint)

    if del_res.status_code == 404:
        print(f"The id {id_key} does not exist")
    elif del_res.status_code == 204:
        print(f"The item with id:{id_key} has been deleted")