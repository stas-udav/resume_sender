#! /usr/bin/env python3
import requests
from Config.indeed_config import *
from Functionality.functions import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException



class JobGraber:
    def __init__(self, driver):
        self.driver = driver

# getting url for scrapping
    def get_url(self, job_website, position):
        url = job_website.format(position)
        return url
    
# Waiting for the page to load
def wait_loading_page(self, timeout, element_xpath):
    try:
        wait = WebDriverWait(self.driver, timeout) 
        # Wait for the page to load
        wait.until(lambda driver: self.driver.find_element(By.XPATH, element_xpath))  
        print("LOADED")
    except TimeoutException:
        print("page loading ERROR")

