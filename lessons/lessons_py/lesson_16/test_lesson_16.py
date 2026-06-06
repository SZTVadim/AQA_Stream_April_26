# импортирвоание модулей
# import math  # математический модуль
import \
    pytest  # Фреймворк, какая-то надстройка, которая расширяет фозможности пайтона (в нашем случае pytest сам нахожит тесты, запускает их, подставляет фикстуры и собирает результат)

"""устанавливаем pip install allure-pytest"""
import requests  # Библиотека, мы сами решаем в каком месте вызвать какой-нибудь запрос (GET или POST и т.д.)

"""устанавливаем pip install requests"""
from math import sqrt, pi, floor

# def test_my_first_test():
#     header = {"accept": "application/json", "Authorization": "Token your_token_here"}
#     # response = requests.get(url="https://petstore.swagger.io/v2/pet/findByStatus?status=available", headers=header,
#     #                         params={"page": 1, "size": 10}, cookies={"session_id": "abc123", "user_pref": "dark_mode"})
#     response = requests.get(url="https://petstore.swagger.io/v2/pet/findByStatus?status=available", headers=header)
#     # assert response.status_code == 404, f"ожидали: 404, получили {response.status_code}"
#     assert response.status_code == 200, f"ожидали: 200, получили {response.status_code}"
#     # print(response)
#     # print(response.status_code)
#     # print(response.json())
#     print(type(response.json()))
#     print(response.text)

# def test_my_second_test():
#     header = {}
#     session = requests.Session()
#     print(header)
#     session.headers.update({"accept": "application/json"})
#
#     response = requests.get(url="https://petstore.swagger.io/v2/pet/findByStatus?status=available", headers=header)
#     print(header)
#     print(response.status_code)
# print(response.headers)
# Заголовки (Headers) в запросах и ответах

headers = {"accept": "application/json"}
respose = requests.post("https://example.org/post", headers=headers)

a = pi
print(a)
print(floor(17 / 5))
print(sqrt(1024))


# Фикстуры
@pytest.fixture
def my_fixture():
    return [1, 2]


@pytest.fixture
def my_fixture_with_teardown():
    print("Начинаем тест, создаем тестовые данные")
    yield [1, 2]
    print("Тест завершен, удаляем тестовые данные")


def test_with_fixture(my_fixture):
    assert sum(my_fixture) == 3


def test_with_fixture_with_teardown(my_fixture_with_teardown):
    assert sum(my_fixture_with_teardown) == 3
