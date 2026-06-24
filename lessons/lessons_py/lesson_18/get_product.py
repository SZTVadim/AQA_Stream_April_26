from lessons.lessons_py.lesson_18.base_api import BaseApi


class GetProduct(BaseApi):

    def get_product(self, id_product):
        return self._request("GET", id_product)

    def get_all_products(self):
        return self._request("GET")
