"""Add SauceDemo login tests here.

Suggested test functions:
- test_valid_login
- test_invalid_password
- test_empty_credentials
- test_locked_out_user
- test_login_page_cross_browser_validation
"""
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from config.config import (
    SAUCE_USERNAME,
    SAUCE_PASSWORD,
    APP_URL,
    BROWSERS
)


@pytest.mark.smoke
@pytest.mark.cross_browser
def test_valid_login(driver):
    

    wait = WebDriverWait(driver, 5)

    driver.find_element(By.ID, "user-name").send_keys(SAUCE_USERNAME)
    driver.find_element(By.ID, "password").send_keys(SAUCE_PASSWORD)
    driver.find_element(By.ID, "login-button").click()

    wait.until(EC.url_contains("inventory.html"))

    assert "inventory.html" in driver.current_url
    assert driver.title == "Swag Labs"

    products = wait.until(
        EC.visibility_of_all_elements_located(
            (By.CLASS_NAME, "inventory_item")
        )
    )

    assert len(products) > 0

@pytest.mark.regression
def test_invalid_login(driver):

   wait =WebDriverWait(driver,5)

   driver.find_element(By.ID, "user-name").send_keys(SAUCE_USERNAME)
   driver.find_element(By.ID, "password").send_keys("wrongpass")
   driver.find_element(By.ID, "login-button").click()

   error=wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "error-message-container")))

   assert error.text == "Epic sadface: Username and password do not match any user in this service"
@pytest.mark.regression
def test_empty_credentials(driver):

    wait = WebDriverWait(driver, 5)
    driver.find_element(By.ID, "login-button").click()

    error = wait.until(
        EC.visibility_of_element_located(
            (By.CLASS_NAME, "error-message-container")
        )
    )

    assert error.text == "Epic sadface: Username is required"

@pytest.mark.regression
def test_locked_out_user(driver):
    
    wait = WebDriverWait(driver, 5)

    driver.find_element(By.ID, "user-name").send_keys("locked_out_user")
    driver.find_element(By.ID, "password").send_keys(SAUCE_PASSWORD)
    driver.find_element(By.ID, "login-button").click()

    error = wait.until( EC.visibility_of_element_located(
            (By.CLASS_NAME, "error-message-container")
        )
    )

    assert error.text == "Epic sadface: Sorry, this user has been locked out."    

@pytest.mark.smoke
@pytest.mark.cross_browser
def test_login_page_cross_browser_validation(driver):
  

    wait = WebDriverWait(driver, 5) 
    assert driver.title == "Swag Labs"
    assert driver.current_url.startswith(APP_URL)

    username = wait.until(
        EC.visibility_of_element_located((By.ID, "user-name"))
    )

    password = driver.find_element(By.ID, "password")
    button = driver.find_element(By.ID, "login-button")

    assert username.is_displayed() and username.is_enabled()
    assert password.is_displayed() and password.is_enabled()
    assert button.is_displayed() and button.is_enabled()
    assert button.text == "Login"