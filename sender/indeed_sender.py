from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from Functionality.functions import *
import time

# Create a new browser instance 
    # Setup
driver = webdriver.Chrome()
    # Fullscrin browser
driver.maximize_window() 

# Load cookie from file
cookies_indeed = load_cookies("indeed_cookies.json")

# Add cookie to the browser session
for cookie in cookies_indeed:
    driver.add_cookie(cookie)

# Open url in browser
driver.get("https://www.indeed.com")

# Waiting for the page to load
wait_loading_page(driver, 5,'//footer[@class="icl-GlobalFooter"]')

# Open new tab with job
