# Практическая часть API
import pytest
# Установить модуль request через команду pip install requests

import requests

from lessons.lessons_py.lesson_17.lesson_17_crud import create_product, delete_product, get_product

# def search_


BASE_URL = "https://practice-api-qa.herokuapp.com"
ENDPOINT = "/api/products"
HEADERS = {"accept": "*/*", "Content-Type": "application/json"}

# JSON_OBJ_1 = {"name": "svs", "description": "any", "price": 999, "quantity": 5}

# response_all_products = requests.get(url=f"{BASE_URL}{ENDPOINT}", headers=HEADERS)
# print(response_all_products.status_code)
# print(response_all_products.json()["data"][0])

# my_products = [x["id"] for x in response_all_products.json()["data"] if x.get("name") and "svs" in x["name"]]
#
# print(my_products)
# def receive_json_for_create(name, description, price, quantity):
#     return {"name": name, "description": description, "price": price, "quantity": quantity}


# data = receive_json_for_create("svs", "any", 999, 5)
# response_create_product = requests.post(url=f"{BASE_URL}{ENDPOINT}", headers=HEADERS, json=data)
# print(response_create_product.status_code)
# print(response_create_product.json())

# id_product = response_create_product.json()["data"]["id"]
# response_delete_product = requests.delete(url=f"{BASE_URL}{ENDPOINT}/{id_product}", headers=HEADERS)
# print(response_delete_product.status_code)
# print(response_delete_product.json())

# оборачиваем все в методы и добавляем ассерты
# def create_product():
#     response = requests.post(url=f"{BASE_URL}{ENDPOINT}", headers=HEADERS, json=data)
#     return response
#
# def delete_product(id_product):
#     response = requests.delete(url=f"{BASE_URL}{ENDPOINT}/{id_product}", headers=HEADERS)
#     return response
#
# def get_product(id_product):
#     response = requests.get(url=f"{BASE_URL}{ENDPOINT}/{id_product}", headers=HEADERS)
#     return response
#
# my_product = create_product()
# id_my_product = my_product.json()["data"]["id"]
# print(my_product)
# print(get_product(id_my_product))
# print(delete_product(id_my_product))
# print(get_product(id_my_product))

def test_create_product():
    try:
        product = create_product()
        assert product.status_code == 201, f" получили {product.status_code}, ожидали 201"
        assert "id" in product.json()["data"], f"{product.json()["data"]}: expected is visible key 'id'"
        assert isinstance(product.json()["data"]["id"], int), f" expect type int, actual :{type(product.json()['data']['id'])}"
    finally:
        delete_product(product.json()["data"]["id"])





def test_delete_product(id_product):
    response =  delete_product(id_product)
    assert response.status_code == 200
    response_get = get_product(id_product)
    assert response_get.status_code == 404
