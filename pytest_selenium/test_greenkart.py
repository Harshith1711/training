import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Create a service object for the Chrome WebDriver
@pytest.fixture(scope="module", autouse=True)
def driver():
    service_obj = Service()

    # Initialize the Chrome WebDriver using the service object
    driver = webdriver.Chrome(service=service_obj)
    yield driver  
    driver.quit()  

@pytest.fixture
def custom_argument():
    return "Ca"   

@pytest.mark.smoke
def test_addcart(driver , custom_argument):
    """
    Search for products and add them to the cart.
    """
    driver.maximize_window()
    time.sleep(5)
    driver.get("https://rahulshettyacademy.com/seleniumPractise#/")
    search = driver.find_element(By.CLASS_NAME, "search-keyword")
    search.send_keys(custom_argument)
    time.sleep(5)
    cart = driver.find_elements(By.CLASS_NAME, "product-action")

    for item in cart:
        item.click()

    items = driver.find_elements(By.XPATH,"//h4[@class='product-name']")
    item_list = []
    for item in items:
        if "-" in item.text:
            item_list.append(item.text.split(" -")[0])
        else:
            item_list.append(item.text)
    assert item_list == ['Cauliflower', 'Carrot', 'Capsicum', 'Cashews']
            
@pytest.mark.smoke
def test_checkout(driver):
    """
    Proceed to checkout and verify the total price.
    """
    checkout = driver.find_element(By.CLASS_NAME, "cart-icon").click()
    cart_items = driver.find_elements(By.CLASS_NAME, "amount")
    x = [int(float(product.text)) for product in cart_items if product.text != '']
    driver.find_element(By.XPATH, "//button[text()='PROCEED TO CHECKOUT']").click()
    time.sleep(5)
    total = driver.find_element(By.XPATH, "//span[@class='totAmt']")
    assert int(total.text) == sum(x)

def test_placeorder(driver):
    """
    Place an order, select the country, agree to T&C, and capture success message.
    """
    place_order = driver.find_element(By.XPATH, "//button[text()='Place Order']")
    place_order.click()
    drop_down = Select(driver.find_element(By.XPATH, "//select"))
    drop_down.select_by_visible_text('India')
    checkbox = driver.find_element(By.CLASS_NAME, "chkAgree")
    checkbox.click()
    driver.find_element(By.XPATH, "//button[text()='Proceed']").click()
    text_val = driver.find_elements(By.XPATH,"//span")
    text_assert = text_val[1].text
    assert text_assert == "Thank you, your order has been placed successfully\nYou'll be redirected to Home page shortly!!"
