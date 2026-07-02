from page.base_page import BasePage


class LoginPage(BasePage):
    USERNAME_SELECTOR = '#user-name'
    PASSWORD_SELECTOR = '#password'
    LOGIN_BUTTON_SELECTOR = '#login-button'

    def __init__(self, page):
        super().__init__(page)
        self._endpoint = ''

    def login(self, username, password):
        self.navigate_to()
        self.wait_for_selector_and_fill(self.USERNAME_SELECTOR, username)
        self.wait_for_selector_and_fill(self.PASSWORD_SELECTOR, password)
        self.wait_for_selector_and_click(self.LOGIN_BUTTON_SELECTOR)
        self.assert_text_present_on_page('Products')

# виды scope в фикстурах
# для каждой функции
# @pytest.fixture(scope="function")
# @pytest.fixture()

# для каждого класса
# @pytest.fixture(scope="class")
# если в файле с тестами у нас 2 класса и ражным набором тестов и надо выполнить фикстуру только для одного из них

# для каждого модуля(файла)
# @pytest.fixture(scope="module")
# для всех тестов в файле

# для всех файлов в папке
# @pytest.fixture(scope="package")

# для всех тестов
# @pytest.fixture(scope="session")



# test
#     test_client
#         test_1
#         test_2
#     test_admin
#         test_4
#         test_3