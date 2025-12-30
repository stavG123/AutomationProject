from selenium.webdriver.common.by import By


def open_login(driver):
    driver.get("https://www.saucedemo.com/")

def do_login(driver, username, password):
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

def get_error_message(driver):
    return driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
