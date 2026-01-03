from ui.pages.login_page import (
    open_login, do_login,
    add_all_products_to_cart, go_to_cart,
    click_checkout, fill_info_and_continue,
    click_finish, is_checkout_complete
)
import time

def test_continue_checkout(driver):
    open_login(driver)
    do_login(driver, "standard_user", "secret_sauce")

    add_all_products_to_cart(driver)
    go_to_cart(driver)
    click_checkout(driver)

    fill_info_and_continue(driver, "John", "Doe", "12345")
    print("after continue url:", driver.current_url)

    click_finish(driver)

    assert is_checkout_complete(driver)
    time.sleep(4)
    print("Checkout completed ✅")
