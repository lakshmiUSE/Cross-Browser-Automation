"""Add SauceDemo login tests here.

Suggested test functions:
- test_valid_login
- test_invalid_password
- test_empty_credentials
- test_locked_out_user
- test_login_page_cross_browser_validation
"""
import pytest


@pytest.mark.smoke
@pytest.mark.cross_browser
def test_valid_login(driver):
    """Replace this starter assertion with the valid-login workflow."""
    assert driver.current_url.startswith("https://www.saucedemo.com/")
