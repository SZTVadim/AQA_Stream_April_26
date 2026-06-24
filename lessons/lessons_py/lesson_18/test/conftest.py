import pytest

from lessons.lessons_py.lesson_18.create_product import CreateProduct
from lessons.lessons_py.lesson_18.delete_product import DeleteProduct
from lessons.lessons_py.lesson_18.get_product import GetProduct
from lessons.lessons_py.lesson_18.utils.utils import payload_for_create_product


@pytest.fixture
def obj_get_product():
    return GetProduct()


@pytest.fixture
def obj_create_product():
    return CreateProduct()


@pytest.fixture
def obj_delete_product():
    return DeleteProduct()


@pytest.fixture
def id_product(obj_create_product) -> int:
    body = payload_for_create_product()
    response = obj_create_product.create_product(payload=body)
    id_product = response.json()["data"]["id"]
    return id_product

@pytest.fixture
def setup_teardown_product(id_product, obj_delete_product):
    yield id_product
    obj_delete_product.delete_product(id_product)

@pytest.fixture
def teardown_product(obj_delete_product):
    list_id_product = []
    yield list_id_product
    for id_product in list_id_product:
        obj_delete_product.delete_product(id_product)
