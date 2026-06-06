import requests

BASE_URL = "https://practice-api-qa.herokuapp.com"
ENDPOINT = "/api/products"
HEADERS_1 = {"accept": "*/*", "Content-Type": "application/json"}
HEADERS_2 = {"accept": "*/*"}

def receive_json_for_create(name, description, price, quantity):
    return {"name": name, "description": description, "price": price, "quantity": quantity}

data = receive_json_for_create("svs", "any", 999, 5)

def create_product():
    response = requests.post(url=f"{BASE_URL}{ENDPOINT}", headers=HEADERS_1, json=data)
    return response

def delete_product(id_product):
    response = requests.delete(url=f"{BASE_URL}{ENDPOINT}/{id_product}", headers=HEADERS_1)
    return response

def get_product(id_product):
    response = requests.get(url=f"{BASE_URL}{ENDPOINT}/{id_product}", headers=HEADERS_1)
    return response