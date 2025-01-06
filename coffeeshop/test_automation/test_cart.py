# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# import time
# import re

# def test_add_to_cart(browser):
#     browser.get("http://127.0.0.1:8000/home")
    
#     coffee = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//h5[normalize-space()='Flat White']")))
#     coffee.click()
#     time.sleep(2)
    
#     add_to_cart_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Add to cart']")))
#     add_to_cart_button.click()
#     time.sleep(2)
    
#     # cart_count = browser.find_element(By.CSS_SELECTOR, "span.cart-count").text
#     # assert int(cart_count) > 0  # Expecting at least 1 item in the cart
    
#     proceed_to_checkout_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,"//a[normalize-space()='Proceed to Checkout']")))
#     proceed_to_checkout_button.click()

# def test_checkout(browser):
#     browser.get("http://127.0.0.1:8000/view_cart/")
    
#     proceed_to_checkout_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH,"//a[normalize-space()='Proceed to Checkout']")))
#     proceed_to_checkout_button.click()
#     time.sleep(2)
    
#     assert browser.current_url == "http://127.0.0.1:8000/checkout/"
    
#     continue_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[@type='submit']")))
#     continue_button.click()
#     time.sleep(2)
    
#     # Extract the current URL
#     current_url = browser.current_url
#     print(f"Current URL: {current_url}")
    
#     # Use a regular expression to match the expected pattern
#     match = re.match(r"http://127\.0\.0\.1:8000/payment/\d+/", current_url)
#     assert match, f"Unexpected URL format: {current_url}"
    
#     # Extract the dynamic part (payment ID) if needed
#     dynamic_payment_id = current_url.split("/")[-2]
#     print(f"Dynamic Payment ID: {dynamic_payment_id}")
    
#     # home_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Home']")))
#     # home_button.click()
#     # time.sleep(3)
    
# def test_payment(browser):
#     browser.get(browser.current_url)
    
#     #Fill out the payment form fields
#     card_no_field = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME,"card-number")))
#     cardholder_name_field = browser.find_element(By.NAME, "card-name")
#     expiry_date_field = browser.find_element(By.NAME, "expiry-date")
#     cvv_field = browser.find_element(By.NAME, "cvv")
#     billing_address_field = browser.find_element(By.NAME, "address")
#     city_field = browser.find_element(By.NAME, "city")
#     pin_code_field = browser.find_element(By.NAME, "postal-code")
    
    
#     card_no_field.send_keys("9475027352")
#     cardholder_name_field.send_keys("testuser")
#     expiry_date_field.send_keys("02/35")
#     cvv_field.send_keys("8796")
#     billing_address_field.send_keys("456 New Coffee")
#     city_field.send_keys("mangalore")
#     pin_code_field.send_keys("574142")
#     time.sleep(3)
    
#     #payment
#     pay_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
#     pay_button.click()
    
#     assert browser.current_url == "http://127.0.0.1:8000/home/"
#     time.sleep(3)
    
    
