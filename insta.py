import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Replace 'YOUR_INSTAGRAM_URL' with the URL of the Instagram profile you want to scrape
url = 'https://www.instagram.com/x_e_n_o_n_19/'

# Create a Selenium WebDriver with options to run in headless mode
options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)  # You'll need to have ChromeDriver installed and in your PATH

# Navigate to the Instagram page
driver.get(url)

# Wait for the follower count element to be visible
wait = WebDriverWait(driver, 20)  # Increase the timeout to 20 seconds or more
try:
    follower_count_element = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@class="g47SY "]')))
    follower_count = follower_count_element.text
    # Extract the post count and following count in a similar manner

    # Print the extracted information
    print("Follower Count:", follower_count)

    # Save the extracted information to a text file
    with open('instagram_stats.txt', 'w') as file:
        file.write(f"Follower Count: {follower_count}\n")

except Exception as e:
    print(f"An error occurred: {str(e)}")

# Close the browser
driver.quit()
