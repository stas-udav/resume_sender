from webbrowser import Chrome
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import json
import datetime


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

def today_date():
    today = datetime.datetime.now().strftime("%d-%m-%Y")
    return today

# Save jobs in json 
def save_jobs_json(jobs_data, filename):
    # Check if data already in existing file
        # Read data from file if file exist
    existing_jobs = {}
    try:
        with open(filename, 'r') as file:
            # Check if file with data
            if file.read().strip():
                # Rolling back the file to the beginning, since we have read it to the end
                file.seek(0)
                # Open existing json file as a dict
                existing_jobs = json.load(file)
                # print(existing_jobs)
    except FileNotFoundError:
        # If file not exist create emphty dict 
        pass
    
    # check duplicates for each job in file
    for job_title, company_name in jobs_data.items():
        # print (jobs_data.items())
        # Create key from company_name + job_title
        key = f'{company_name}-{job_title}'
        if key not in existing_jobs:
            # If this key not exist in file we add in new dict
            existing_jobs[job_title] = company_name, today_date()
    # existing_jobs.update(new_job_data)

    # Save data in file
    # if new_job_data:
    with open(filename, 'w') as f:
        #indent=4: Этот аргумент указывает на отступ в
            #4 пробела для удобочитаемости выходного JSON-файла.
        json.dump(existing_jobs, f, indent=4) 
