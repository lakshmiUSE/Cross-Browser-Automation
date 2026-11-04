# Selenium Cross-Browser Automation Testing

## Project overview
A Python, Selenium WebDriver, and Pytest starter framework for testing the SauceDemo login flow across Chrome, Firefox, and Microsoft Edge.

Application: https://www.saucedemo.com/

## Folder structure
```text
selenium-cross-browser-testing/
├── config/
│   ├── __init__.py
│   └── config.py
├── tests/
│   ├── __init__.py
│   └── test_login.py
├── screenshots/
│   └── .gitkeep
├── reports/
│   └── .gitkeep
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Setup (Windows)
```powershell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

Edit `.env` if needed. The sample SauceDemo credentials are public practice credentials.
Do not commit `.env` or any real credentials.

## Run tests
Run configured browsers (Chrome, Firefox, Edge):
```bash
pytest -v --html=reports/report.html --self-contained-html
```

Run one browser:
```bash
pytest -v --browser=chrome
pytest -v --browser=firefox
pytest -v --browser=edge
```

Headless:
```bash
pytest -v --browser=chrome --headless
```

Markers:
```bash
pytest -v -m smoke
pytest -v -m regression
```

Parallel execution (optional):
```bash
pytest -v -n 3
```

## Implementation tasks
Complete `tests/test_login.py` with the required valid login, invalid password, empty credentials, locked-out user, and cross-browser UI checks. Add explicit waits with `WebDriverWait` and expected conditions. Do not use `time.sleep()`.

Implement screenshot capture after successful login and on test failure. Store screenshots in `screenshots/`.

## Notes
- Selenium Manager can manage compatible browser drivers automatically in supported Selenium versions.
- Chrome, Firefox, and Edge must be installed on the machine.
- The included test is a starter smoke test, not the complete assignment solution.
- Only record actual browser results in the final cross-browser summary; do not assume all browsers pass.
