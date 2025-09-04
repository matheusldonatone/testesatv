from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://the-internet.herokuapp.com/login")


    username_input = driver.find_element(By.ID, "username")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')

    username_input.send_keys("tomsmith")
    password_input.send_keys("SuperSecretPassword!")

    login_button.click()

    time.sleep(2)

    if "secure" in driver.current_url:
        print("Login realizado com sucesso!")
    else:
        print("Falha no login.")

finally:
    time.sleep(2)
    driver.quit()
