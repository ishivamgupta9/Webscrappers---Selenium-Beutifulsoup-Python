from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import json
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
driver.get("http://dover.ias-clt.com/")


streetkey="ACACIA PL";
streetnokey=10;

streetno= driver.find_element(By.NAME, "parcel.search[p_adrno]")

streetno.send_keys(streetnokey)


streetname= driver.find_element(By.NAME,"parcel.search[p_street]")

streetname.send_keys(streetkey)



submit= driver.find_element(By.NAME,"parcel.search[search]")
submit.click()
time.sleep(4)
# Find the element by the provided XPath
page_source = driver.page_source

# Use BeautifulSoup to parse the page source
soup = BeautifulSoup(page_source, 'html.parser')

# Find all the text on the page
all_text = soup.get_text()

# You can print or save the 'all_text' as per your requirements
# print(all_text)


lines = all_text.split('\n')

# Initialize variables to store owner names
owner1_name = None
owner2_name = None

# Loop through the lines to find owner names
for i, line in enumerate(lines):
    if "Owner 1 Name:" in line:
        owner1_name = lines[i + 1].strip()
    elif "Owner 2 Name:" in line:
        owner2_name = lines[i + 1].strip()

# Print the owner names
print("Owner 1 Name:", owner1_name)
print("Owner 2 Name:", owner2_name)

appraised_land_value = None
appraised_building_value = None
total_value = None

# Loop through the lines to find assessed values
for line in lines:
    if "Appraised Land:" in line:
        appraised_land_value = line.split("Appraised Land:")[-1].strip()
    elif "Appraised Bldg:" in line:
        appraised_building_value = line.split("Appraised Bldg:")[-1].strip()
    elif "Total:" in line:
        total_value = line.split("Total:")[-1].strip()

assessed_values = {}

# Loop through the lines to find assessed values
current_label = None

for line in lines:
    line = line.strip()  # Remove leading and trailing spaces
    if line in ["Appraised Land:", "Appraised Bldg:", "Total:"]:
        current_label = line
    elif current_label:
        assessed_values[current_label] = line
        current_label = None

# Print the assessed values
for label, value in assessed_values.items():
    print(f"{label}: {value}")




pdf_save_path = "output.pdf"
pdfkit_options = {
    "page-size": "A4",
    "margin-top": "0mm",
    "margin-right": "0mm",
    "margin-bottom": "0mm",
    "margin-left": "0mm",
    "no-images": None,
}

# # Generate the PDF
# pdfkit.from_file("path/to/your/html/file.html", pdf_save_path, options=pdfkit_options)


# Define the path where you want to save the HTML content
html_save_path = r"C:\Users\1234\Downloads\New folder (2)\your2_file.html"

# Save the HTML content to the specified file
with open(html_save_path, "w", encoding="utf-8") as html_file:
    html_file.write(page_source)

# Define the path where you want to save the PDF file
pdf_save_path = r"C:\Users\1234\Downloads\New folder (2)\output.pdf"



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

# Close the WebDriver
driver.quit()