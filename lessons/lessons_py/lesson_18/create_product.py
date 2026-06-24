from lessons.lessons_py.lesson_18.base_api import BaseApi


class CreateProduct(BaseApi):

    def create_product(self, payload):
        return self._request("POST", json=payload)


