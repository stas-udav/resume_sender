from xml.dom.minidom import Element
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, TimeoutException
from selenium.webdriver.support import expected_conditions as EC
import time
from Functionality.functions import save_sent_jobs, wait_element, input_keys, random_sleep, wait_elements, today_date
from Functionality.functions import click, create_login_window
import re
import json
import os
from selenium.common.exceptions import JavascriptException

username, password = create_login_window()
# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
    # Fullscrin browser
driver.maximize_window()
# Open dice
driver.get("https://www.dice.com/dashboard/login")

# Create an ActionChains object
action = ActionChains(driver)

# Login, input email and than next page is password input
wait_element(driver, '//input[@type="email"]')
input_keys(driver, '//input[@type="email"]', username)
click(driver, '//button[@type="submit"]')
wait_element(driver, '//input[@placeholder="Enter Password"]')
input_keys(driver, '//input[@placeholder="Enter Password"]', password)
wait_element(driver,'//dhi-seds-nav-footer')
click(driver, '//button[@data-testid="submit-password"]')
random_sleep(0.1, 3)

# Checking pop up and close if present
# try:
#     if wait_element(driver, '//div[@class="fe-popup-content"]'):   
#         time.sleep(1) 
#         driver.find_element(By.XPATH, '//div[@class="fe-popup-cross"]').click()       
#     else:    
#         pass
# except TimeoutException:
#     print("Element not found. Proceeding with other actions...")
random_sleep(0.1, 3)

# Searching for job possition by filters  
# //button[@id="reload-button"]
driver.get("https://www.dice.com/jobs")
try:
    while True:
        button = driver.find_element(By.XPATH, '//button[@id="reload-button"]')
        button.click()    
        
except NoSuchElementException:
    print("Page loaded successfully")
    
# location_btn = driver.find_element(By.XPATH,'//button[@id="IPGeoLocateButton"]')
# action.move_to_element(location_btn).perform()
wait_element(driver,'//dhi-seds-nav-footer')
time.sleep(2)
input_keys(driver, '//input[@id="typeaheadInput"]', "Software qa")
random_sleep(0.1, 3)
submit_search_button = driver.find_element(By.XPATH, '//button[@id="submitSearch-button"]')
submit_search_button.click()
random_sleep(1, 3)
#  Remote  
work_setting = ['Hybrid', 'Last 3 Days', 'Yes'] 
for filter in work_setting:
    set_element = wait_element(driver, f"//div[@id='searchFacetsDesktop']//*[normalize-space(text())= '{filter}']")
    action.move_to_element(set_element).perform()
    time.sleep(1) 
    driver.execute_script("arguments[0].click();", set_element)
    random_sleep(0.3, 0.5)    
    print(set_element.text)

# Going through jobs, click on them and save date, apply
# next_page_disbled = wait_element(driver, '//li[@class="pagination-next page-item ng-star-inserted disabled"]')

# print(os.getcwd()) 
currend_dir = os.getcwd()
alredy_sent_jobs = os.path.join(currend_dir, 'jobs_dice.json') #'jobs_dice.json'
with open(alredy_sent_jobs, 'r') as f:
    if os.path.getsize(alredy_sent_jobs) == 0:
        print('file is empty')
        alredy_sent_jobs = {}
    else:
        alredy_sent_jobs = json.load(f)
        # print(alredy_sent_jobs)
count_saved_jobs = 0
while True:
    next_page_btn = wait_element(driver, '//li[@class="pagination-next page-item ng-star-inserted"]')
    job_data = {}
    # disabled_next_page_btn = wait_element(driver, '//li[@class="pagination-next page-item ng-star-inserted disabled"]')
    
    jobs = driver.find_elements(By.XPATH, '//a[@data-cy="card-title-link"]')
    num_el = len(jobs)
    # print(num_el)на
    saved_jobs = 0
    # already_sent_jobs = {}
    time.sleep(1)
    for i in range(num_el):
        # print(i) 
        print(num_el)
        # if i >= len(jobs):
        #     print("Page is over, found {saved_jobs} jobs")
        #     break
        try:                           
            # print('break')      
            # break
            job = jobs[i]
            print(job.text)
            time.sleep(2)
            # Scroll to the top of the page before clicking the job
            driver.execute_script("window.scrollTo(0, 0);")
            # driver.execute_script("arguments[0].scrollIntoView(true);", job)
            random_sleep(3, 10)
            action.move_to_element(job).click().perform()
            random_sleep(1, 3)          
            # check domain
            driver.switch_to.window(driver.window_handles[-1])
            new_url = driver.current_url            
            # print(new_url)
            # check if the new url is from dice.com domain
            # if not, that means it's an external url and we should not apply
            # if it's a dice.com url, continue with the loop
            if not re.match(r'^https://www\.dice\.com/', new_url):
                # if it's an external url, print a message and break the loop
                print("external url")
                driver.back()
                continue
            else:                
                job_title = driver.find_element(By.XPATH, '//h1[@data-cy="jobTitle"]')
                job_title_text = job_title.text            
                print(job_title_text)
                job_id = driver.find_element(By.XPATH, '//apply-button-wc')
                job_id_text = job_id.get_attribute('job-id')
                print(job_id_text)
                company_name = driver.find_element(By.XPATH, '//a[@data-cy="companyNameLink"]')
                company_name_text = company_name.text
                print(company_name_text)
                if job_id_text in alredy_sent_jobs:
                    print(f'JOB = {job_title_text} already SENT, skipping...')
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0]) 
                    continue
                alredy_sent_jobs[job_id_text] = [job_title_text, company_name_text, today_date()]         
                wait_element(driver, '//dhi-seds-nav-footer')
                wait_element(driver, '//div[@id="buttons"]')              
                  
                time.sleep(5)
                apply = driver.execute_script('return document.querySelector("#applyButton > apply-button-wc").shadowRoot.querySelector("apply-button > div > button")')
                try:
                    driver.execute_script('arguments[0].click();', apply)
                except JavascriptException as e:
                    print(f" {i} Alredy applied: {e}")
                    alredy_sent_jobs[job_id_text] = [job_title_text, company_name_text, today_date()]
                    print(alredy_sent_jobs)
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0]) 
                    continue
                wait_element(driver, '//dhi-seds-nav-footer')
                next_btn = wait_element(driver, '//button[@class="seds-button-primary btn-next"]')
                next_btn.click()
                try:
                    submit_btn = wait_element(driver, '//button[span/text()="Submit"]')
                    random_sleep(0.5, 2.5)
                    submit_btn.click()
                    # time.sleep(10)
                    # save_jobs_json(job_data, "jobs_dice.json") 
                    saved_jobs += 1
                    random_sleep(1, 3)
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])            
                    # print (saved_jobs) 
                    random_sleep(1, 9)
                    count_saved_jobs += 1
                    print(f"saved {saved_jobs} jobs")                   
                    save_sent_jobs('jobs_dice.json', alredy_sent_jobs)
                    # save_jobs_json
                    print(i)
                except Exception as e:
                    print(f"not a standart apply {e}")
                    driver.close()
                    driver.switch_to.window(driver.window_handles[0])
                    print(i) 
                    continue
    
        except StaleElementReferenceException as e:
            print(f"StaleElementReferenceException {i}: {e}")
            continue 
    try:
        disabled_next_page_btn = driver.find_element(By.XPATH, '//li[@class="pagination-next page-item ng-star-inserted disabled"]')
        break  # Exit loop if "Next Page" is disabled
    except NoSuchElementException:
        pass  # Continue if "Next Page" is not disabled
    if i == num_el - 1:
        action.move_to_element(next_page_btn).perform()
        time.sleep(2)
        next_page_btn.click()
        time.sleep(2)
        print("Page is over, click on next page")
        random_sleep(3, 10)
  