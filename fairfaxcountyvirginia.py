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
driver.get("https://icare.fairfaxcounty.gov/ffxcare/search/commonsearch.aspx?mode=address")


streetkey="WOODLAND FALLS";
streetnokey=10986;

streetno= driver.find_element(By.NAME, "inpNumber")

streetno.send_keys(streetnokey)


streetname= driver.find_element(By.NAME,"inpStreet")

streetname.send_keys(streetkey)



submit= driver.find_element(By.NAME,"btSearch")
submit.click()
time.sleep(4)
# Find the element by the provided XPath
page_source = driver.page_source

# Use BeautifulSoup to parse the page source
soup = BeautifulSoup(page_source, 'html.parser')

# Find all the text on the page
text = soup.get_text()

# You can print or save the 'all_text' as per your requirements
print(text)

# Split the text by specific labels
owner_name = re.search(r'OwnerName([^,]+)', text).group(1).strip()

# Extract land area (e.g., "(SQFT)75,041")
land_area_match = re.search(r'\(SQFT\)([\d,]+)', text)
land_area = land_area_match.group(1) if land_area_match else None

# Extract property location
property_location_match = re.search(r'Property Location(.+?)Map', text)
property_location = property_location_match.group(1).strip() if property_location_match else None

# Print the extracted information
print("Owner Name:", owner_name)
print("Land Area (SQFT):", land_area)
print("Property Location:", property_location)
# This code searches for the pattern (SQFT) followed by digits and commas to extract the value like (SQFT)75,041. It should provide you with the desired output.











# ss

# total_width = driver.execute_script("return document.body.offsetWidth")
# total_height = driver.execute_script("return document.body.scrollHeight")

# # Set the window size to the webpage's dimensions
# driver.set_window_size(total_width, total_height)

# # Initialize variables for scrolling
# current_height = 0
# scroll_height = total_height

# # Set the path to save the screenshots
# save_path = "Image/"

# # Scroll and capture screenshots
# while current_height < scroll_height:
#     driver.save_screenshot(save_path + f"screenshot_{current_height}.png")
#     current_height += 2000  # You can adjust the scrolling distance (e.g., 1000 pixels)

#     # Scroll down
#     driver.execute_script(f"window.scrollTo(0, {current_height});")

# Wait for the page to load completely (you can adjust the waiting time)
time.sleep(5)
driver.execute_script("document.body.style.zoom='80%'")  # Example: Set zoom level to 80%

# Set the path to save the screenshots
save_path = "Image/"

# Capture the first screenshot
driver.save_screenshot(save_path + "screenshot_0.png")

# # Get the webpage's dimensions
# total_height = driver.execute_script("return document.body.scrollHeight")

# # Initialize variables for scrolling
# current_height = 1000
# scroll_height = total_height
# scroll_step = 1000  # Adjust this value to control scrolling distance

# # Scroll and capture overlapping screenshots
# while current_height < scroll_height:
#     current_height += scroll_step

#     if current_height > scroll_height:
#         current_height = scroll_height  # Ensure not to overshoot

#     # Scroll to the current height
#     driver.execute_script(f"window.scrollTo(0, {current_height});")

#     # Wait for a moment to allow content to load (you can adjust the waiting time)
#     time.sleep(2)

#     # Capture a screenshot
#     driver.save_screenshot(save_path + f"screenshot_{current_height}.png")




# values_link = driver.find_element(By.XPATH, "//li[@class='unsel']/a/span[text()='Values']")

# # Click the "Values" link
# values_link.click()

# time.sleep(2)


# values

driver.get("https://icare.fairfaxcounty.gov/ffxcare/datalets/datalet.aspx?mode=valuesall&sIndex=0&idx=1&LMparent=138");



valuetext = soup.get_text()

# You can print or save the 'all_text' as per your requirements
print("Valuepage data------------->  ",valuetext)










time.sleep(4)
# # Close the WebDriver
driver.quit()