import pytest

from lessons.lessons_py.lesson_17.lesson_17_crud import create_product


@pytest.fixture
def id_product():
    return create_product().json()["data"]["id"]