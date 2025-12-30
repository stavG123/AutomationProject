from ui.pages.login_page import open_login, do_login

def test_login_success(driver):
    open_login(driver)
    do_login(driver, "standard_user", "secret_sauce")
    assert "inventory" in driver.current_url.lower()

def test_login_wrong_password(driver):
    open_login(driver)
    do_login(driver, "standard_user", "wrong_pass")
    assert "saucedemo" in driver.current_url.lower() 
    assert False

