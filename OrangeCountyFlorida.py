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

driver.get("https://ocpaweb.ocpafl.org/parcelsearch")

time.sleep(4)

address="5287 Stone Harbour Rd"
addressbox=driver.find_element(By.ID,"PropertyAddress");
addressbox.send_keys(address);
time.sleep(10)


addressbox.send_keys(Keys.RETURN) 

time.sleep(20)
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'html.parser')

# # Find all the text on the page
text = soup.get_text()


print(text)




print_icon = driver.find_element(By.XPATH, '//li[@aria-label="Print Property Card, opens in a new window"]/a')

# Click on the print icon
print_icon.click()

time.sleep(20)




button = driver.find_element(By.XPATH,"/html/body/ngb-modal-window/div/div/app-print-settings/div[2]/form/div[2]/button[1]")

# Click the button
button.click()


time.sleep(20)



# Use PyAutoGUI to press Ctrl+P to open the print dialog
pyautogui.hotkey('ctrl', 'p')
time.sleep(2)  # Wait for the print dialog to appear


pyautogui.press('enter')
time.sleep(40)  # Increase the waiting time if needed

driver.quit()