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

    # Enter valid credentials
    username_field.send_keys("tomsmith")
    password_field.send_keys("SuperSecretPassword!")

    print("Entered valid username and password.")

    # Step 3: Locate and click the login button
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()

    print("Clicked login button.")

    # Step 4: Wait for the page to load and click the logout button
    time.sleep(5)
    logout_button = driver.find_element(By.XPATH, "//a[@href='/logout']")
    logout_button.click()

    print("Clicked logout button.")

    # Step 5: Verify redirection to the login page
    time.sleep(5)  # Wait for the page to load
    assert "Login Page" in driver.title, "Logout failed: Did not return to login page."

    print("Logout test passed: Redirected to login page.")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the browser
    driver.quit()
