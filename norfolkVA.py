from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import re
import pdfkit
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
driver = webdriver.Chrome()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=chrome_options)
# Set the page load timeout to 5 minutes (300,000 milliseconds)
driver.set_page_load_timeout(300000)
from PIL import Image
driver.get("https://air.norfolk.gov/#/")


addresskey="400 E Virginia Beach Boulevard";
# //streetnokey=10986;

address= driver.find_element(By.ID, "primary_search")

address.send_keys(addresskey)





address.send_keys(Keys.RETURN) 

time.sleep(4)

# address.send_keys(Keys.RETURN) 

# time.sleep(4)
# Find the element by the provided XPath
page_source = driver.page_source

# Use BeautifulSoup to parse the page source
soup = BeautifulSoup(page_source, 'html.parser')

# Find all the text on the page
text = soup.get_text()

# You can print or save the 'all_text' as per your requirements
print(text)


owner_name_match = re.search(r'Owner Name([\s\S]*?)Property Address', text)
if owner_name_match:
    owner_name = owner_name_match.group(1).strip()

property_address_match = re.search(r'Property Address([\s\S]*?)([A-Z\d\s]+)', text)
if property_address_match:
    property_address = property_address_match.group(2).strip()

legal_description_match = re.search(r'Legal Description([\s\S]*?)(\w+\s+\d+\.\d+\s+Ft)', text)
if legal_description_match:
    legal_description = legal_description_match.group(2).strip()

total_value_match = re.search(r'Total Value([\s\S]*?)', text)
if total_value_match:
    total_value = total_value_match.group(1).strip()

acreage_match = re.search(r'Parcel Approximate Acreage\s*:\s*([\d.]+ acres)', text)
if acreage_match:
    parcel_acreage = acreage_match.group(1).strip()

# Print the extracted information
print("Owner Name:", owner_name)
print("Property Address:", property_address)
print("Legal Description:", legal_description)
print("Total Value:", total_value)
# print("Parcel Approximate Acreage:", parcel_acreage)



# ss

time.sleep(5)
driver.execute_script("document.body.style.zoom='80%'")  # Example: Set zoom level to 80%

# Set the path to save the screenshots
save_path = "Image/"

# Capture the first screenshot
driver.save_screenshot(save_path + "screenshot_0.png")

# Get the webpage's dimensions
total_height = driver.execute_script("return document.body.scrollHeight")

# Initialize variables for scrolling
current_height = 1000
scroll_height = total_height
scroll_step = 1000  # Adjust this value to control scrolling distance

# Scroll and capture overlapping screenshots
while current_height < scroll_height:
    current_height += scroll_step

    if current_height > scroll_height:
        current_height = scroll_height  # Ensure not to overshoot

    # Scroll to the current height
    driver.execute_script(f"window.scrollTo(0, {current_height});")

    # Wait for a moment to allow content to load (you can adjust the waiting time)
    time.sleep(2)

    # Capture a screenshot
    driver.save_screenshot(save_path + f"screenshot_{current_height}.png")







time.sleep(4)

















# # Close the WebDriver
driver.quit()