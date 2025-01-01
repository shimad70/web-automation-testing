from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Set up ChromeDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

try:
    # Step 1: Open the login page
    driver.get("https://the-internet.herokuapp.com/login")
    driver.maximize_window()

    # Step 2: Locate and fill in the username and password fields
    username_field = driver.find_element(By.ID, "username")
    password_field = driver.find_element(By.ID, "password")

    username_field.send_keys("tomsmith")
    password_field.send_keys("SuperSecretPassword!")

    print("Entered username and password.")

    # Step 3: Locate and click the login button
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    print("Clicked login button.")

    # Step 4: Wait for the page to load and check for specific content
    time.sleep(5)  # Adjust wait time if necessary
    page_content = driver.page_source

    # Verify login success by checking page content
    assert "Welcome to the Secure Area" in page_content, "Login failed: Welcome message not found."

    print("Login test passed: Welcome message found.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
