import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope="module")
def browser():
    options = Options()
    # options.add_argument("--headless")
    driver = webdriver.Firefox(options=options)
    yield driver
    driver.quit()