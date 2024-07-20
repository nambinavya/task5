from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import time

# Initialize the WebDriver
driver = webdriver.Chrome()  # Make sure the ChromeDriver is in your PATH
driver.maximize_window()

# Function to log test results
def log_result(message):
    with open('test_results.log', 'a') as f:
        f.write(message + '\n')
    print(message)

# Function to test if an element exists
def element_exists(by, value):
    try:
        driver.find_element(by, value)
        return True
    except NoSuchElementException:
        return False

# Function to test the homepage
def test_homepage():
    try:
        driver.get("https://example.com")  # Replace with your website URL
        time.sleep(2)
        
        # Check if the main elements are present
        if element_exists(By.ID, "header"):
            log_result("Header is present on the homepage.")
        else:
            log_result("Header is missing on the homepage.")
        
        if element_exists(By.ID, "footer"):
            log_result("Footer is present on the homepage.")
        else:
            log_result("Footer is missing on the homepage.")
        
        if element_exists(By.NAME, "search"):
            log_result("Search bar is present on the homepage.")
        else:
            log_result("Search bar is missing on the homepage.")
        
    except WebDriverException as e:
        log_result(f"Error during homepage test: {e}")

# Function to test the login functionality
def test_login():
    try:
        driver.get("https://example.com/login")  # Replace with your login page URL
        time.sleep(2)
        
        username_field = driver.find_element(By.NAME, "username")
        password_field = driver.find_element(By.NAME, "password")
        login_button = driver.find_element(By.ID, "loginBtn")
        
        username_field.send_keys("testuser")  # Replace with a test username
        password_field.send_keys("testpassword")  # Replace with a test password
        login_button.click()
        
        time.sleep(2)
        
        if element_exists(By.ID, "dashboard"):
            log_result("Login successful and dashboard is accessible.")
        else:
            log_result("Login failed or dashboard is not accessible.")
        
    except NoSuchElementException as e:
        log_result(f"Error during login test: {e}")

# Function to test the contact form
def test_contact_form():
    try:
        driver.get("https://example.com/contact")  # Replace with your contact page URL
        time.sleep(2)
        
        name_field = driver.find_element(By.NAME, "name")
        email_field = driver.find_element(By.NAME, "email")
        message_field = driver.find_element(By.NAME, "message")
        submit_button = driver.find_element(By.ID, "submitBtn")
        
        name_field.send_keys("Test User")
        email_field.send_keys("testuser@example.com")
        message_field.send_keys("This is a test message.")
        submit_button.click()
        
        time.sleep(2)
        
        if element_exists(By.CLASS_NAME, "success-message"):
            log_result("Contact form submitted successfully.")
        else:
            log_result("Failed to submit the contact form.")
        
    except NoSuchElementException as e:
        log_result(f"Error during contact form test: {e}")

# Run the tests
test_homepage()
tes
