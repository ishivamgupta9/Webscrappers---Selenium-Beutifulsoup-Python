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
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors')


driver.set_page_load_timeout(300)

driver.get("https://www.polkpa.org/CamaDisplay.aspx?OutputMode=Input&searchType=RealEstate&page=FindByAddress&cookie_test=true")

time.sleep(4)

address="3378 WINCHESTER ESTATES CIR"
addressbox=driver.find_element(By.ID,"address");
addressbox.send_keys(address);
time.sleep(10)


addressbox.send_keys(Keys.RETURN) 

time.sleep(20)
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# # Find all the text on the page
text = soup.get_text()

# You can print or save the 'all_text' as per your requirements
# print(text)
pattern = r'(\d{2}-\d{2}-\d{2}-\d{6}-\d{6})'
matches = re.findall(pattern, text)

# Check if there are any matches and store the first one in a variable
if matches:
    parcel_id = matches[0]
    print("Parcel ID:", parcel_id)
else:
    print("No parcel ID found in the text.")
time.sleep(15)

# Locate the hyperlink within the table
table = driver.find_element(By.TAG_NAME, "table")
hyperlink = table.find_element(By.PARTIAL_LINK_TEXT,  parcel_id)
driver.execute_script("arguments[0].click();", hyperlink)





time.sleep(20)
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# # Find all the text on the page
text = soup.get_text()

# You can print or save the 'all_text' as per your requirements
print(text)



# Locate the "Property Record Card" hyperlink
prc_hyperlink = driver.find_element(By.XPATH, "//a[contains(@href, 'PRCReport/viewPRC.aspx')]")
prc_url = prc_hyperlink.get_attribute("href")

# Check if the hyperlink is not None before navigating
if prc_url:
    driver.get(prc_url)
    time.sleep(40)
    driver.quit()
else:
    print("Property Record Card hyperlink not found.")

time.sleep(40)



time.sleep(40)















driver.quit()