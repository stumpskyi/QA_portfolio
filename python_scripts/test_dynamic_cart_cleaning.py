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
def test_cart_cleanup_logic(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()
    wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".inventory_item")))
    buttons = driver.find_elements(By.CSS_SELECTOR, "[id^='add-to-cart']")
    for button in buttons[:3]:
        button.click()
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    remove_buttons = driver.find_elements(By.XPATH, "//button[text()='Remove']")
    print(f"Buttons to remove: {len(remove_buttons)}")
    while remove_buttons:
        btn = remove_buttons[0]
        btn.click()
        wait.until(EC.staleness_of(btn))
        remove_buttons = driver.find_elements(By.XPATH, "//button[text()='Remove']")
    try:
        wait.until(EC.invisibility_of_element_located((By.CLASS_NAME, "shopping_cart_badge")))
        print("Badge disappeared as expected")
    except:
        print("Badge is still visible!")
    cart_text = driver.find_element(By.CLASS_NAME, "shopping_cart_link").text
    assert cart_text == "", f"FAILED! Expected empty cart, but got '{cart_text}'"