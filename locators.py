from selenium.webdriver.common.by import By

INPUT_USERNAME = (By.ID, "user-name")
INPUT_PASSWORD = (By.ID, "password")
LOGIN_BUTTON = (By.ID, "login-button")

LOGIN_ERROR_MESSAGE = (By.CSS_SELECTOR, 'h3[data-test="error"]')

INVENTORY_LIST_PARENT = (By.CSS_SELECTOR, 'div[data-test="inventory_list"]')
