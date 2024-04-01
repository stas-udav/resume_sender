#! /usr/bin/env python3
import requests
from Config.indeed_config import *
from Functionality.functions import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time

# Create a new browser instance 
    # Setup
driver = webdriver.Chrome()
    # Fullscrin browser
driver.maximize_window() 

# getting url for scrapping
indeed_search_url = get_url("software+qa", indeed_job_search_3days)
print(indeed_search_url)

# open url in browser
driver.get(indeed_search_url)

# Waiting for the page to load
wait_loading_page(driver, 5,'//footer[@class="icl-GlobalFooter"]')

# searching for job by cretaria
# job = {}
jobs = driver.find_elements(By.XPATH, '//div[@data-testid="slider_item"]')
print(len(jobs))

# click on job_description to open side menu with "apply button" and click on "apply button"

for job in jobs:
    job.click()
    time.sleep(1)
    #searching for apply button
    try:
        apply_button = driver.find_element(By.XPATH, '//div[@class="ia-IndeedApplyButton"]')    
        job_title = job.text.split('\n')[0].strip()
        print(job_title)        
    except NoSuchElementException:
        print("Apply on company web-site", job.get_attribute("title"))
    



