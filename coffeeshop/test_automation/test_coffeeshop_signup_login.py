from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_signup(browser):
    browser.get("http://127.0.0.1:8000/signup/")
    
    #Fill out the form fields
    username_field = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME,"username")))
    fname_field = browser.find_element(By.NAME,"first_name")
    lname_field = browser.find_element(By.NAME,"last_name")
    mobile_field = browser.find_element(By.NAME, "mobile_number")
    email_field = browser.find_element(By.NAME, "email")
    password1_field = browser.find_element(By.NAME, "password1")
    password2_field = browser.find_element(By.NAME, "password2")
    
    username_field.send_keys("testuser2")
    fname_field.send_keys("test")
    lname_field.send_keys("user2")
    mobile_field.send_keys("1234567890")
    email_field.send_keys("testuser@example.com")
    password1_field.send_keys("testpassword123")
    password2_field.send_keys("testpassword123")
    time.sleep(2)

    submit_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    submit_button.click()
    
    # WebDriverWait(browser, 20).until(EC.url_to_be("http://127.0.0.1:8000/login/"))
    # assert browser.current_url == "http://127.0.0.1:8000/login/"
    
def test_login(browser):

    browser.get("http://127.0.0.1:8000/login/")
    
    username_field = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.NAME, "username")))
    password_field = browser.find_element(By.NAME, "password")
    
    username_field.send_keys("testuser1")
    password_field.send_keys("testpassword123")
    time.sleep(2)
    
    login_button = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']")))
    login_button.click()

    assert browser.current_url == "http://127.0.0.1:8000/home/"
    
