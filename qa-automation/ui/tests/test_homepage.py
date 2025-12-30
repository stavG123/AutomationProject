from ui.pages.login_page import open_login, do_login, get_error_message
import pytest # type: ignore

def test_login_success(driver):
    open_login(driver)
    do_login(driver, "standard_user", "secret_sauce")
    assert "inventory" in driver.current_url.lower()

def test_login_wrong_password(driver):
    open_login(driver)
    do_login(driver, "standard_user", "wrong_pass")
    assert "saucedemo" in driver.current_url.lower()
    error_message = get_error_message(driver)
    assert error_message.is_displayed()


