import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--guest")
    options.add_argument("--disable-features=SafeBrowsing")
    driver_instance = webdriver.Chrome(options=options)
    driver_instance.maximize_window()
    yield driver_instance
    driver_instance.quit()
def test_complete_order_flow(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    add_btn = wait.until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-backpack")))
    add_btn.click()
    cart_link = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_link")))
    cart_link.click()
    checkout_btn = wait.until(EC.element_to_be_clickable((By.ID, "checkout")))
    checkout_btn.click()
    wait.until(EC.visibility_of_element_located((By.ID, "first-name"))).send_keys("Vlad")
    driver.find_element(By.ID, "last-name").send_keys("Test")
    driver.find_element(By.ID, "postal-code").send_keys("12345")
    driver.find_element(By.ID, "continue").click()
    finish_btn = wait.until(EC.element_to_be_clickable((By.ID, "finish")))
    finish_btn.click()
    header_element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "complete-header")))
    assert header_element.text == "Thank you for your order!", f"Error: Got '{header_element.text}'"
    print("SUCCESS: E2E Order Test Passed!")