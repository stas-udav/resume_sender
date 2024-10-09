#! /usr/bin/env python3
import requests
from Config.indeed_config import *
from Functionality.functions import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException




class JobGraber:
    def __init__(self, driver, job_website):
        self.link = job_website
        self.driver = driver

# getting url for scrapping
    def get_url(self, position):
        url = self.link.format(position)
        return url

    def set_pages(self, num_pages):
        self.num_pages = num_pages
# Waiting for the page to load
def wait_loading_page(self, timeout, element_xpath):
    try:
        wait = WebDriverWait(self.driver, timeout) 
        # Wait for the page to load
        wait.until(lambda driver: self.driver.find_element(By.XPATH, element_xpath))  
        print("LOADED")
    except TimeoutException:
        print("page loading ERROR")


dice = JobGraber(driver, "www.dice.com")
dice.set_pages(10)
