from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

chrome_options = Options()
chrome_options.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_options)

try:
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    time.sleep(3)  # espera a página carregar

    username_input = driver.find_element(By.NAME, "username")
    password_input = driver.find_element(By.NAME, "password")
    login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')

    username_input.send_keys("Admin")
    password_input.send_keys("admin123")

    login_button.click()

    time.sleep(5)  # espera a página redirecionar

    if "dashboard" in driver.current_url:
        print("Login realizado com sucesso!")
    else:
        print("Falha no login.")

finally:
    time.sleep(2)
    driver.quit()
