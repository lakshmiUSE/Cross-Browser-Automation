import pytest
from selenium import webdriver
from config.config import BROWSERS, APP_URL


@pytest.fixture(params=BROWSERS)
def driver(request):

    browser = request.param

    if browser == "chrome":
        driver = webdriver.Chrome()

    elif browser == "firefox":
        driver = webdriver.Firefox()

    elif browser == "edge":
        driver = webdriver.Edge()

    driver.maximize_window()
    driver.get(APP_URL)

    yield driver

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    
    if report.when == "call":
        driver = item.funcargs.get("driver")

        if driver:
            if report.passed:
                driver.save_screenshot(
                    f"screenshots/{item.name}_passed.png"
                )

            elif report.failed:
                driver.save_screenshot(
                    f"screenshots/{item.name}_failed.png"
                )    