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

    drv = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
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