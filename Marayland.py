from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pdfkit

from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(options=chrome_options)
# Set the page load timeout to 5 minutes (300,000 milliseconds)
driver.set_page_load_timeout(300000)

driver.get("https://sdat.dat.maryland.gov/RealProperty/Pages/default.aspx")

# Locate the <select> element by its ID using the find_element method
select_county = driver.find_element(By.ID, "cphMainContentArea_ucSearchType_wzrdRealPropertySearch_ucSearchType_ddlCounty")
select_method = driver.find_element(By.ID, "cphMainContentArea_ucSearchType_wzrdRealPropertySearch_ucSearchType_ddlSearchType")

# Create a Select object to interact with the <select> element
selectcounty = Select(select_county)
selectcounty.select_by_visible_text("BALTIMORE COUNTY")

selecttype = Select(select_method)
selecttype.select_by_visible_text("STREET ADDRESS")

# Click the "Continue" button and navigate to the next page
continue_button = driver.find_element(By.CLASS_NAME, "btnNext")
continue_button.click()
        
time.sleep(4)

street_number = driver.find_element(By.ID, "cphMainContentArea_ucSearchType_wzrdRealPropertySearch_ucEnterData_txtStreenNumber")
street_number.send_keys("8630")

street_name = driver.find_element(By.ID, "cphMainContentArea_ucSearchType_wzrdRealPropertySearch_ucEnterData_txtStreetName")
street_name.send_keys("SILVER LAKE")

continue_button = driver.find_element(By.CLASS_NAME, "btnNext")
continue_button.click()
        
time.sleep(4)


time.sleep(5)
driver.execute_script("document.body.style.zoom='60%'")  # Example: Set zoom level to 80%

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




driver.execute_script("window.print();")





driver.quit()