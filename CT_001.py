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
  
    driver.get("https://www.saucedemo.com/")

    username_input = driver.find_element(By.ID, "user-name")
    password_input = driver.find_element(By.ID, "password")
    login_button = driver.find_element(By.ID, "login-button")

    username_input.send_keys("standard_user")
    password_input.send_keys("secret_sauce")

    login_button.click()

    time.sleep(2)

    if "inventory.html" in driver.current_url:
        print("Login realizado com sucesso!")
    else:
        print("Falha no login.")

finally:
    time.sleep(2)
    driver.quit()
