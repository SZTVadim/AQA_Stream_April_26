from lessons.lessons_py.lesson_18.base_api import BaseApi


class DeleteProduct(BaseApi):

    def delete_product(self, id_product):
        return self._request("DELETE", id_product)
