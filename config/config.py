"""Project configuration loaded from environment variables."""
import os

APP_URL = os.getenv("APP_URL", "https://www.saucedemo.com/")
SAUCE_USERNAME = os.getenv("SAUCE_USERNAME", "standard_user")
SAUCE_PASSWORD = os.getenv("SAUCE_PASSWORD", "secret_sauce")
BROWSERS = os.getenv("BROWSERS", "chrome,firefox,edge").split(",")
