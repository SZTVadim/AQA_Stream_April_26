from lessons.lessons_py.lesson_18.utils.utils import payload_for_create_product


class TestProduct:
    def test_delete_product(self, obj_delete_product, obj_get_product, id_product):
        response = obj_delete_product.delete_product(id_product)
        assert response.status_code == 200, f"ожидали: 200, получили: {response.status_code}"

        response_get = obj_get_product.get_product(id_product)
        assert response_get.status_code == 404, f"ожидали: 404, получили: {response_get.status_code}"


    def test_get_product(self, setup_teardown_product, obj_get_product):
        response = obj_get_product.get_product(id_product=setup_teardown_product)
        data_for_response = response.json()["data"]

        assert response.status_code == 200
        assert isinstance(data_for_response["id"], int)
        assert isinstance(data_for_response["price"], float)
        assert isinstance(data_for_response["quantity"], int)
        assert isinstance(data_for_response["description"], str)
        assert isinstance(data_for_response["name"], str)

    def test_create_product(self, obj_create_product, teardown_product):
        body = payload_for_create_product("svs1", "anyy", 1011, 55)
        response = obj_create_product.create_product(body)
        data_for_response = response.json()["data"]
        teardown_product.append(data_for_response["id"])

        assert response.status_code == 201
        assert data_for_response["name"] == body["name"]
        assert data_for_response["description"] == body["description"]
        assert data_for_response["price"] == body["price"]
        assert data_for_response["quantity"] == body["quantity"]

    def test_create_product_with_empty_name(self, obj_create_product, teardown_product):
        body = payload_for_create_product("")
        response = obj_create_product.create_product(body)
        assert response.status_code == 400
        assert response.json()["error"] == "[Поле имя не может быть пустым]"

        # data_for_response = response.json()["data"]
        # teardown_product.append(data_for_response["id"])
        #
        # assert response.status_code == 201
        # assert data_for_response["name"] == body["name"]
        # assert data_for_response["description"] == body["description"]
        # assert data_for_response["price"] == body["price"]
        # assert data_for_response["quantity"] == body["quantity"]



    # # удалить все продукты по очереди
    # def test_delete_all_products(self, obj_delete_product, obj_get_product):
    #     response_get = obj_get_product.get_all_products().json()
    #     ids_products: list[int] = [p["id"] for p in response_get["data"]]
    #     for id_product in ids_products:
    #         obj_delete_product.delete_product(id_product)

