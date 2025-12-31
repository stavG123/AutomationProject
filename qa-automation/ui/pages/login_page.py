from selenium.webdriver.common.by import By
import time


def open_login(driver):
    driver.get("https://www.saucedemo.com/")

def do_login(driver, username, password):
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

def get_error_message(driver):
    return driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")

def add_all_products_to_cart(driver):
    buttons = driver.find_elements(By.CLASS_NAME, "btn_inventory")
    for btn in buttons:
        btn.click()
    return len(buttons)

def go_to_cart(driver):
    cart_link = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_link.click()
    return

def checkout(driver):
    checkout_button = driver.find_element(By.CSS_SELECTOR, ".checkout_button")
    checkout_button.click()


def fill_checkout_info(driver, first_name, last_name, postal_code):
    driver.find_element(By.ID, "first-name").send_keys(first_name)
    driver.find_element(By.ID, "last-name").send_keys(last_name)
    driver.find_element(By.ID, "postal-code").send_keys(postal_code)
    
def continue_checkout(driver):
    driver.find_element(By.ID, "continue").click()



   