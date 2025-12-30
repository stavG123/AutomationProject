from selenium.webdriver.common.by import By

def open_login(driver):
    driver.get("https://www.saucedemo.com/")

def do_login(driver, username, password):
    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()
