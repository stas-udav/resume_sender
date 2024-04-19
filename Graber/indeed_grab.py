#! /usr/bin/env python3
from Config.indeed_config import *
from Functionality.functions import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pandas as pd
import time
import random
import datetime

# Create a new browser instance 
    # Setup
driver = webdriver.Chrome()
    # Fullscrin browser
driver.maximize_window() 

# getting url for scrapping
indeed_search_url = get_url("software+qa", indeed_job_search_3days)

# open url in browser
driver.get(indeed_search_url)

# Waiting for the page to load
wait_loading_page(driver, 5,'//footer[@class="icl-GlobalFooter"]')

# click on job_description to open side menu with "apply button" and click on "apply button"
job_title_links = {}
next_page = driver.find_element(By.XPATH, '//a[@data-testid="pagination-page-next"]')

# checking all jobs on page while script reach last page
while next_page:

    # searching for job by cretaria
    jobs = driver.find_elements(By.XPATH, '//div[@data-testid="slider_item"]')
    # print(len(jobs))
    saved_jobs = 0

    # iterate thru jobs by each job possition
    for job in jobs:

        # check if amount of grabbed jobs equals jobs on page
        if saved_jobs < len(jobs):        
            job.click()
            time.sleep(1)        
            saved_jobs +=1
            # print(saved_jobs)
            
            #searching for apply button (direct apply on indeed)
            try:
                time.sleep(1)
                apply_button = driver.find_element(By.XPATH, '//div[@class="ia-IndeedApplyButton"]')    
                job_title = job.text.split('\n')[0].strip()
                print(job_title)
                job_link = job.find_element(By.XPATH, '//a').get_attribute('href')
                # company_name_job = job.text.split('\n')[4].strip()
                company_name = job.find_element(By.XPATH, './/span[@data-testid="company-name"]').text
                # print (apply_button.text)
                print(job_link)
                print(company_name)                
                job_title_links[job_title] = [job_link, company_name, datetime.datetime.now().strftime("%d-%m-%Y")]
                time.sleep(random.uniform(1, 10))  

            # if applying only on company web-site we skipped              
            except NoSuchElementException:
                print("Apply on company web-site", job.get_attribute("title"))  
                time.sleep(random.uniform(1, 3))  
    save_jobs_json(job_title_links, "jobs_indeed.json")                        
    # else: 
    print("End od Page")
    print(saved_jobs)
    # Check if next page button exists and clicking on next page, updating varibles saved_jobs, jobs for new vallue from next page
    next_page = driver.find_element(By.XPATH, '//a[@data-testid="pagination-page-next"]')
    if next_page:            
        driver.implicitly_wait(3)
        next_page.click()        
        jobs = driver.find_elements(By.XPATH, '//div[@data-testid="slider_item"]')
        saved_jobs = 0
        time.sleep(random.uniform(1, 2))    
# push next page after all jobs was grabbed
else: 
    print("last page done!")
    print(job_title_links)

# convert dictionary to a dataframe
# df = pd.DataFrame(list(job_title_links.items()), columns=['Title', 'Link'])

# write the dataframe object into excel file
# df.to_excel("output1.xlsx", index=False, header=True)
# print(job_title_links)    
        # print(job_title_links)


