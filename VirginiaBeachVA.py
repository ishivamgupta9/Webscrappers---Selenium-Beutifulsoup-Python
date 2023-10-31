from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
import re
import pyautogui
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from PIL import Image
driver = webdriver.Chrome()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors')





# Set the page load timeout to 5 minutes (300,000 milliseconds)
driver.set_page_load_timeout(30000)

driver.get("https://propertysearch.virginiabeach.gov/#/")

#


addresskey="2401 ADAIR CT";
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


# Extract "Total Value," "Owner," and "Land" using regular expressions
total_value_match = re.search(r"Total Value\$([\d,]+)", text)
if total_value_match:
    total_value = total_value_match.group(1)

owner_match = re.search(r"Owner 1(.+?)(?:Owner 2|$)", text)
if owner_match:
    owner = owner_match.group(1).strip()

sf_match = re.search(r'(\d{1,3}(?:,\d{3})*(?:\.\d+)?\s*SF)', text)
if sf_match:
    sf_value = sf_match.group(1).strip()

# Print the extracted "9,371.08 SF"

# Print the extracted information
print("Total Value:", total_value)
print("Owner:", owner)
print("Square Footage:", sf_value)

legal_description_match = re.search(r'Legal Description([\s\S]*?)([A-Z\d\s]+)', text)
if legal_description_match:
    legal_description = legal_description_match.group(2).strip()

# Print the extracted legal description
print("Legal Description:", legal_description)


chrome_options.add_argument('--headless')  # Run Chrome in headless mode
chrome_options.add_argument('--disable-gpu')  # Disable GPU to avoid potential issues

# Wait for the page to load (you can adjust the waiting time)
time.sleep(5)

# Set the zoom level (if needed)
driver.execute_script("document.body.style.zoom='50%'")  

# Set the path to save the screenshots
save_path = "Image/"

# Capture the first screenshot
driver.save_screenshot(save_path + "VIRGINIABEACH_1.png")


# Set up the Selenium web driver (replace 'your_driver_path' with the actual path to your Chrome driver executable)


# Set the path to save the PDF file
pdf_save_path = "Image2/"

time.sleep(5)

# Use PyAutoGUI to press Ctrl+P to open the print dialog
pyautogui.hotkey('ctrl', 'p')
time.sleep(2)  # Wait for the print dialog to appear


pyautogui.press('enter')
time.sleep(25)  # Increase the waiting time if needed

driver.quit()
