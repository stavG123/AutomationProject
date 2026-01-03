import pytest # type: ignore
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import os

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1400,900")

    # Use a clean temporary browsing session (helps a lot)
    options.add_argument("--incognito")
    options.add_argument("--disable-notifications")

    # Disable Chrome password manager + leak detection popups
    options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "password_manager_leak_detection": False,
        "profile.default_content_setting_values.notifications": 2,
    })

    # Disable Chromium “password leak detection” features (the popup you saw)
    options.add_argument("--disable-features=PasswordLeakDetection,PasswordManagerEnablePasswordsLeakCheck")

    drv = webdriver.Chrome(options=options)
    yield drv
    drv.quit()
    

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()

    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("driver")
        if not driver:
            return

        os.makedirs("reports", exist_ok=True)

        filename = f"{item.name}.png"
        filepath = os.path.join("reports", filename)

        driver.save_screenshot(filepath)

        html = item.config.pluginmanager.getplugin("html")
        if html:
            rep.extra = getattr(rep, "extra", [])
            rep.extra.append(html.extras.image(filename))