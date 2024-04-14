from webbrowser import Chrome
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import json


# Getting url for job searching
def get_url(position, website):
    url = website.format(position)
    return url

# Waiting for the page to load
def wait_loading_page(driver, timeout, element_xpath):
    try:
        wait = WebDriverWait(driver, timeout) 
        # Wait for the page to load
        wait.until(lambda driver: driver.find_element(By.XPATH, element_xpath))  
        print("LOADED")
    except TimeoutException:
        print("page loading ERROR")
    time.sleep(1)

def find_job():
    pass

# Save jobs in json
def save_jobs_json(jobs_data, filename):
    with open(filename, 'a') as f:
        #indent=4: Этот аргумент указывает на отступ в
            #4 пробела для удобочитаемости выходного JSON-файла.
        json.dump(jobs_data, f, indent=4) 
