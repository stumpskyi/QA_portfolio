import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
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
def test_price_sorting(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    sort_container = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "product_sort_container")))
    select = Select(sort_container)
    select.select_by_visible_text("Price (low to high)")
    prices = driver.find_elements(By.CLASS_NAME, "inventory_item_price")
    lowest_price = float(prices[0].text.replace("$", ""))
    highest_price = float(prices[-1].text.replace("$", ""))
    print(f"Checking: {lowest_price} < {highest_price}")
    assert lowest_price < highest_price, "Sorting failed!"