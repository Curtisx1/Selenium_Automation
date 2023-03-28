from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

# Define the path to the Chrome driver
chrome_driver_path = 'path/to/chromedriver'

# Define a function to check the warranty of a serial number
def check_warranty(serial):
    # Create a Chrome driver instance
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(chrome_driver_path, options=chrome_options)

    # Navigate to the HP warranty check webpage
    driver.get('https://support.hp.com/us-en/checkwarranty')

    # Find the input box for the serial number and enter the serial number
    input_box = driver.find_element_by_name('serialNumber')
    input_box.send_keys(serial)
    input_box.send_keys(Keys.RETURN)

    # Wait for the warranty status and expiration date to load
    time.sleep(2)

    # Find the warranty status and expiration date in the HTML
    warranty_status = driver.find_element_by_css_selector('div.status').text.strip()
    expiration_date = driver.find_element_by_css_selector('div.date').text.strip()

    # Quit the Chrome driver instance
    driver.quit()

    # Return the warranty status and expiration date
    return warranty_status, expiration_date
