from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set up ChromeDriver using Service
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open a website
driver.get("https://example.com")

# Print the page title
print("Page title is:", driver.title)

# Close the browser
driver.quit()
