import allure
from pages.login_page import LoginPage as login_page


@allure.title("Тестирование успешного логина с валидными данными")
def test_correct_login_standart_user(browser):

    page = login_page(browser)

    page.open_page().login(
        "standard_user", "secret_sauce"
    ).get_current_url_after_some_actions("https://www.saucedemo.com/inventory.html")


@allure.title("Тестирование логина с неверным паролем")
def test_login_with_uncorrect_password(browser):

    page = login_page(browser)

    error_message = (
        "Epic sadface: Username and password do not match any user in this service"
    )

    page.open_page().login("standard_user", "111").check_error_message(error_message)


@allure.title("Тестирование логина заблокированного пользователя")
def test_login_blocked_user(browser):

    page = login_page(browser)

    error_message = "Epic sadface: Sorry, this user has been locked out."
    page.open_page().login("locked_out_user", "secret_sauce").check_error_message(
        error_message
    )


@allure.title("Тестирование логина с пустыми полями")
def test_login_empty_fields(browser):

    page = login_page(browser)

    error_message = "Epic sadface: Username is required"
    page.open_page().login("", "").check_error_message(error_message)


@allure.title(
    "Тестирование успешного логина пользователя 'performance_glitch_user' и перехода на страницу товаров"
)
def test_correct_login_performance_user(browser):

    page = login_page(browser)

    page.open_page().login(
        "performance_glitch_user", "secret_sauce"
    ).get_current_url_after_some_actions(
        "https://www.saucedemo.com/inventory.html"
    ).check_load_elements()
