from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def open_login(driver):
    driver.get("https://www.saucedemo.com/")


def do_login(driver, username, password):
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()


def add_all_products_to_cart(driver):
    buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    for btn in buttons:
        btn.click()
    return len(buttons)


def go_to_cart(driver):
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()


def click_checkout(driver):
    # SauceDemo checkout button is id="checkout"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    ).click()


def fill_info_and_continue(driver, first_name, last_name, postal_code):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys(first_name)
    driver.find_element(By.ID, "last-name").send_keys(last_name)
    driver.find_element(By.ID, "postal-code").send_keys(postal_code)
    wait.until(EC.element_to_be_clickable((By.ID, "continue"))).click()


def click_finish(driver):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "finish"))
    ).click()


def is_checkout_complete(driver) -> bool:
    # The exact text appears in class="complete-header"
    header = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "complete-header"))
    )
    return "Thank you for your order!" in header.text
