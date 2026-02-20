import os
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope="module")
def browser():
    remote_url = os.getenv("SELENOID_REMOTE_URL", "http://localhost:4444/wd/hub")
    options = Options()

    selenoid_options = {
        "enableVNC": True, 
        "enableVideo": False,
        "screenResolution": "1280x1024x24"  
    }

    options.set_capability("browserName", "firefox")
    options.set_capability("selenoid:options", selenoid_options)

    driver = webdriver.Remote(command_executor=remote_url, options=options)
    yield driver
    driver.quit()
