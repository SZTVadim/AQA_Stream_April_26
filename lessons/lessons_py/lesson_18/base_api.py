import requests


class BaseApi:
    BASE_URL = "https://practice-api-qa.herokuapp.com"
    ENDPOINT = "/api/products"
    HEADERS = {"accept": "*/*"}


    def _request(self, method, id_product=None, **kwargs):
        if id_product:
            url = f"{self.BASE_URL}{self.ENDPOINT}/{id_product}"
        else:
            url = f"{self.BASE_URL}{self.ENDPOINT}"
        return requests.request(method, url, headers=self.HEADERS, **kwargs)

