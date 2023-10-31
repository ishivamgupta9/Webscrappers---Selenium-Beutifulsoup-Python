from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pyautogui
import json
import re
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from PIL import Image
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=chrome_options)
# Set the page load timeout to 5 minutes (300,000 milliseconds)
driver.set_page_load_timeout(300000)
driver.get("https://apps.richmondgov.com/applications/PropertySearch/Search.aspx")



tab=driver.find_element(By.ID,"MainContent_tcPropertySearch_tcPropertyAddress_tab");
tab.click()

streetk="Chamberlayne Ave";
street=2305;

streetno=driver.find_element(By.ID,"MainContent_tcPropertySearch_tcPropertyAddress_txtBlgNumMin");
# <input name="ctl00$MainContent$tcPropertySearch$tcPropertyAddress$txtBlgNumMin" type="text" value="2305" id="MainContent_tcPropertySearch_tcPropertyAddress_txtBlgNumMin" class="width50px">
streetno.send_keys(street);


streetkey=driver.find_element(By.ID,"MainContent_tcPropertySearch_tcPropertyAddress_txtStName");
streetkey.send_keys(streetk);

# <input name="ctl00$MainContent$tcPropertySearch$tcPropertyAddress$txtStName" type="text" value="Chamberlayne" onchange="javascript:setTimeout('__doPostBack(\'ctl00$MainContent$tcPropertySearch$tcPropertyAddress$txtStName\',\'\')', 0)" onkeypress="if (WebForm_TextBoxKeyHandler(event) == false) return false;" id="MainContent_tcPropertySearch_tcPropertyAddress_txtStName" autocomplete="off">

time.sleep(4)

search=driver.find_element(By.ID,"MainContent_btnSubmit");
search.click()


# time.sleep(30)
# searchmain=driver.find_element(By.CLASS_NAME,"searchHover");
# searchmain.click()


time.sleep(30)

element = driver.find_element(By.XPATH, "//tr[@class='searchRow']")

# Click on the element using execute_script()
driver.execute_script("arguments[0].click();", element)

time.sleep(30)

page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# # Find all the text on the page
text = soup.get_text()

# You can print or save the 'all_text' as per your requirements
print(text)

time.sleep(15)

# Use regular expressions to extract information
owner_match = re.search(r'Owner:\s+(.*?)\n', text)
parcel_square_feet_match = re.search(r'Parcel Square Feet:\s+([\d.]+)', text)
acreage_match = re.search(r'Acreage:\s+([\d.]+)', text)
land_value_match = re.search(r'Land Value:\s+\$([\d,]+)', text)
improvement_value_match = re.search(r'Improvement Value:\s+\$([\d,]+)', text)
total_value_match = re.search(r'Total Value:\s+\$([\d,]+)', text)

# Extract the values if the matches are found
owner = owner_match.group(1) if owner_match else None
parcel_square_feet = parcel_square_feet_match.group(1) if parcel_square_feet_match else None
acreage = acreage_match.group(1) if acreage_match else None
land_value = land_value_match.group(1) if land_value_match else None
improvement_value = improvement_value_match.group(1) if improvement_value_match else None
total_value = total_value_match.group(1) if total_value_match else None

# Print the extracted values
print("Owner:", owner)
print("Parcel Square Feet:", parcel_square_feet)
print("Acreage:", acreage)
print("Land Value:", land_value)
print("Improvement Value:", improvement_value)
print("Total Value:", total_value)


chrome_options.add_argument('--headless')  # Run Chrome in headless mode
chrome_options.add_argument('--disable-gpu')  # Disable GPU to avoid potential issues

# Wait for the page to load (you can adjust the waiting time)
time.sleep(5)

# Set the zoom level (if needed)
driver.execute_script("document.body.style.zoom='50%'")  

# Set the path to save the screenshots
save_path = "Image/"

# Capture the first screenshot
driver.save_screenshot(save_path + "richmond.png")


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

