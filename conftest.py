import os
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope="module")
def browser():
    remote_url = os.getenv("SELENOID_REMOTE_URL", "http://localhost:4444/wd/hub")
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Remote(command_executor=remote_url, options=options)
    yield driver
    driver.quit()
