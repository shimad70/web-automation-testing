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

    # Enter invalid credentials
    username_field.send_keys("invalid_user")
    password_field.send_keys("wrong_password")

    print("Entered invalid username and password.")

    # Step 3: Locate and click the login button
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    print("Clicked login button.")

    # Step 4: Wait for the error message and verify it
    time.sleep(5)  # Adjust wait time if necessary
    error_message = driver.find_element(By.ID, "flash").text

    assert "Your username is invalid!" in error_message, "Error message not displayed for invalid login."

    print("Negative login test passed: Error message displayed as expected.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
