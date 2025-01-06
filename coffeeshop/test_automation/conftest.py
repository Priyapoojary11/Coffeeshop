import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = None
    
@pytest.fixture(scope="session", autouse=True)
def browser():
    
    #With & Without data available
    service = Service(executable_path=r'C:\Users\priya\Downloads\chromedriver-win64\chromedriver-win64\chromedriver.exe')
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    # driver.get("http://127.0.0.1:8000/")
    driver.maximize_window()
    yield driver
    driver.quit()
    
    #With data available   
    # global driver
    # if driver is None:
        
    #     driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    #     driver.maximize_window()
    #     yield driver
    #     driver.quit()
    # return driver
