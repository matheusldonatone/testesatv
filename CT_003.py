from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("http://practicetestautomation.com/practice-test-login")

    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "submit")

    username_input.send_keys("student")
    password_input.send_keys("Password123")

    login_button.click()

    time.sleep(2)

    if "logged-in-successfully" in driver.current_url:
        print("Login realizado com sucesso!")
    else:
        print("Falha no login.")

finally:
    time.sleep(2)
    driver.quit()
