#! /usr/bin/env python3
from pydoc import cli
from Config.indeed_config import *
from Functionality.functions import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

import os
import time
import random


# Create a new browser instance 
    # torn off google security login check
# options = Options()
# profile = "C:\\Users\\stanh\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 3"
# options.add_argument(f"user-data-dir={profile}")
#     # Setup
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
    # Fullscrin browser
driver.maximize_window()
# driver.get("https://www.google.com/") 
# time.sleep(2)
# click(driver, '//span[@class="gb_Kd"]')
# time.sleep(2)
# input_keys(driver,'//input[@type="email"]', 'stan.se.gordon@gmail.com')
# time.sleep(2)
# click(driver, '//button[@class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b"]')


# loggin into accaunt utilizing googl acc
driver.get("https://secure.indeed.com/auth?hl=en_US&co=US&continue=https%3A%2F%2Fwww.indeed.com%2F%3Ffrom%3Dgnav-homepage&tmpl=desktop&from=gnav-util-homepage&jsContinue=https%3A%2F%2Fonboarding.indeed.com%2Fonboarding%3Fhl%3Den_US%26co%3DUS%26from%3Dgnav-homepage&empContinue=https%3A%2F%2Faccount.indeed.com%2Fmyaccess")
wait_loading_page(driver, 5, '//footer[@class="icl-GlobalFooter"]')
input_keys(driver, '//input[@name="__email"]', "stan.se.gordon@gmail.com")
# wait_loading_page(driver,3, '//button[@type="submit"]')
# indeed_google_login_button = driver.find_element(By.XPATH '//button[@id="login-google-button"]')
time.sleep(random.uniform(1,7))
click(driver, '//button[@type="submit"]')
# click(driver, '//button[@id="login-google-button"]')
time.sleep(random.uniform(1,7))
click(driver, '//a[@id="auth-page-google-otp-fallback"]')
# click(driver, '//button[@id="gsuite-login-google-button"]')
time.sleep(random.uniform(1,7))
gmail_read("imap.gmail.com", "stan.se.gordon@gmail.com", "Skaya2301!", "Indeed one-time passcode")

# switch to login pop_up window
# original_window = driver.window_handles[0]
# google_login_page = driver.window_handles[-1]
# driver.switch_to.window(google_login_page)
# input_keys(driver,'//input[@type="email"]', 'stan.se.gordon@gmail.com')
# time.sleep(random.uniform(1,7))
# click(driver, '//button[@class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b"]')
# time.sleep(13)
# # pass credantials from env verable
# user = os.environ.get("indeed_username")

# getting url for scrapping
indeed_search_url = get_url("software+qa", indeed_job_search_3days)

# open url in browser
driver.get(indeed_search_url)

# Waiting for the page to load
wait_loading_page(driver, 5,'//footer[@class="icl-GlobalFooter"]')

# Сlick on job_description to open side menu with "apply button" and click on "apply button"
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
                company_name = job.find_element(By.XPATH, '.0//span[@data-testid="company-name"]').text
                # print (apply_button.text)
                print(job_link)
                print(company_name)                
                job_title_links[job_title] = [job_link, company_name, today_date()]
                print(today_date())
                time.sleep(random.uniform(1, 10))  
                
            # if applying only on company web-site we skipped              
            except NoSuchElementException:
                print("Apply on company web-site", job.get_attribute("title"))  
                time.sleep(random.uniform(1, 3))  
    if job_title_links:
        save_jobs_json(job_title_links, "jobs_indeed_test2456.json")                        
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

driver.quit