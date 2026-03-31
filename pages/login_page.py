from pages.base_page import BasePage
import urls
import allure
import locators


class LoginPage(BasePage):

    @allure.step("Открываем страничку логина в браузере")
    def open_page(self):
        self.open(urls.LOGIN_PAGE_URL)
        return self

    @allure.step("Заполняем поле логина (юзернейм)")
    def fill_username(self, username):
        self.fill_input(locators.INPUT_USERNAME, username)
        return self

    @allure.step("Заполняем поле пароля")
    def fill_password(self, password):
        self.fill_input(locators.INPUT_PASSWORD, password)
        return self

    @allure.step("Жмем на кнопку логина")
    def click_login_button(self):
        login_button = self.find_element(locators.LOGIN_BUTTON)
        login_button.click()
        return self

    @allure.step(
        "Входим в систему под именем пользователя '{username}' и с паролем = '{password}'"
    )
    def login(self, username, password):
        self.fill_username(username)
        self.fill_password(password)
        self.click_login_button()
        return self

    @allure.step(
        "Ищем окно сообщения об ошибке при некорректном логине и проверяем его содержимое"
    )
    def check_error_message(self, expect_message):
        try:
            error_message = self.find_element(locators.LOGIN_ERROR_MESSAGE).text
            with allure.step("Сверяем ожидаемое сообщение и полученное"):
                assert (
                    error_message == expect_message
                ), f"Появилось сообщение '{error_message}' вместо ожидаемого '{expect_message}'"
        except:
            return "Сообщения об ошибке не обнаружено при условии наличия ошибки!"

    @allure.step("Получаем текущий URL после некоторых действия пользователя")
    def get_current_url(self):
        return self.get_url()

    @allure.step("Проверка открытия ожидаемого URL")
    def get_current_url_after_some_actions(self, expected_part, timeout=15):
        try:
            current_url = self.wait_url_contains(expected_part, timeout)
            return self
        except:
            return "Ожидаемый URL не загрузился!"

    @allure.step(
        "Проверка загрузки и отображения элементов на странице после входа в систему"
    )
    def check_load_elements(self):
        try:
            items = self.find_elements(locators.INVENTORY_LIST_PARENT)
            with allure.step("Проверяем, что товары загрузились и отобразились"):
                assert (
                    len(items) != 0
                ), "Списка товаров нет, скорее всего страница не загрузилась"
                return self
        except:
            return "Элементы не загрузились!"
