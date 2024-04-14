from Classes.GraberClasses.ScanInded import IndeedGraber
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from Config import indeed_config
import time

# Create a new browser instance 
    # Setup
driver = webdriver.Chrome()
    #   Fullscreen browser
driver.maximize_window()

# getting url for scrapping
indeed = IndeedGraber(driver)
indeed_url = indeed.get_url(indeed_config.indeed_job_search_3days, "software+qa")
print(indeed_url)

# open indeed job offers url
driver.get(indeed_url)

# # waiting for loading page
indeed.wait_loading_page(5, '//footer[@class="icl-GlobalFooter"]')