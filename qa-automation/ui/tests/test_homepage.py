from ui.pages.login_page import open_login, do_login, get_error_message,add_all_products_to_cart
import pytest # type: ignore
from selenium.webdriver.common.by import By


def test_login_success(driver):
    open_login(driver)
    do_login(driver, "standard_user", "secret_sauce")
    assert "inventory" in driver.current_url.lower()

def test_login_wrong_password(driver):
    # GIVEN
    open_login(driver)
    # WHEN
    do_login(driver, "standard_user", "wrong_pass")
    # THEN
    assert "inventory" not in driver.current_url.lower()
    error_message = get_error_message(driver)
    assert error_message.is_displayed()

def test_add_all_products_to_cart(driver):
    # GIVEN
    open_login(driver)
    do_login(driver, "standard_user", "secret_sauce")

    # WHEN
    added_count = add_all_products_to_cart(driver)

    # THEN
    cart_badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge")
    assert int(cart_badge.text) == added_count
    print(f"Added {added_count} products to the cart successfully.")



