from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support import expected_conditions as EC
import time, datetime
from Functionality.functions import wait_element, input_keys, random_sleep, wait_elements, today_date, save_jobs_json
from Functionality.functions import click
import re

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
input_keys(driver, '//input[@type="email"]', "stan.hordon@gmail.com")
click(driver, '//button[@type="submit"]')
wait_element(driver, '//input[@placeholder="Enter Password"]')
input_keys(driver, '//input[@placeholder="Enter Password"]', "skaya2301")
wait_element(driver,'//dhi-seds-nav-footer')
click(driver, '//button[@data-testid="submit-password"]')
random_sleep(0.1, 3)

# Checking pop up and close if present
if wait_element(driver, '//div[@class="fe-popup-content"]'):   
    time.sleep(1) 
    driver.find_element(By.XPATH, '//div[@class="fe-popup-cross"]').click()       
else:    
    pass

random_sleep(0.1, 3)

# Searching for job possition by filters
driver.get("https://www.dice.com/jobs")
# location_btn = driver.find_element(By.XPATH,'//button[@id="IPGeoLocateButton"]')
# action.move_to_element(location_btn).perform()
wait_element(driver,'//dhi-seds-nav-footer')
time.sleep(2)
input_keys(driver, '//input[@id="typeaheadInput"]', "Software QA")
random_sleep(0.1, 3)
submit_search_button = driver.find_element(By.XPATH, '//button[@id="submitSearch-button"]')
submit_search_button.click()
random_sleep(1, 3)

work_setting = ['Remote', 'Last 3 Days', 'Yes']
for filter in work_setting:
    set_element = wait_element(driver, f"//div[@id='searchFacetsDesktop']//*[normalize-space(text())= '{filter}']")
    time.sleep(0.2) 
    set_element.click()
    time.sleep(0.1)
    print(set_element.text)

# Going through jobs, click on them and save date, apply
# next_page_disbled = wait_element(driver, '//li[@class="pagination-next page-item ng-star-inserted disabled"]')

# page = 0
while True:
    next_page_btn = wait_element(driver, '//li[@class="pagination-next page-item ng-star-inserted"]')
    job_data = {}
    # disabled_next_page_btn = wait_element(driver, '//li[@class="pagination-next page-item ng-star-inserted disabled"]')
    if not next_page_btn :
        break
    jobs = driver.find_elements(By.XPATH, '//a[@data-cy="card-title-link"]')
    num_el = len(jobs)
    print(num_el)
    saved_jobs = 0
    time.sleep(1)
    for i in range(num_el):
        # if i >= len(jobs):
        #     print("Page is over, found {saved_jobs} jobs")
        #     break
        try:
            # Перезахват элемента внутри цикла
            # jobs = driver.find_elements(By.XPATH, '//a[@data-cy="card-title-link"]')
            job = jobs[i]
            action.move_to_element(job).click().perform()
            random_sleep(1, 3)          
            # check domain
            driver.switch_to.window(driver.window_handles[-1])
            new_url = driver.current_url            
            # print(new_url)
            # check if the new url is from dice.com domain
            # if not, that means it's an external url and we should not apply
            if not re.match(r'^https://www\.dice\.com/', new_url):
                # if it's an external url, print a message and break the loop
                print("external url")
                driver.back()
                continue
            else:
                # if it's a dice.com url, continue with the loop
                job_title = driver.find_element(By.XPATH, '//h1[@data-cy="jobTitle"]')
                job_title_text = job_title.text            
                print(job_title_text)
                company_name = driver.find_element(By.XPATH, '//a[@data-cy="companyNameLink"]')
                company_name_text = company_name.text
                print(company_name_text)
                job_data[job_title_text] = [ company_name_text, today_date()]
                wait_element(driver, '//dhi-seds-nav-footer')
                wait_element(driver, '//div[@id="buttons"]')
                time.sleep(5)
                apply = driver.execute_script('return document.querySelector("#applyButton > apply-button-wc").shadowRoot.querySelector("apply-button > div > button")')
                driver.execute_script('arguments[0].click();', apply)
                time.sleep(10)
                # save_jobs_json(job_data, "jobs_dice.json") 
                random_sleep(1, 3)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
            saved_jobs += 1
            print (saved_jobs)
        except StaleElementReferenceException as e:
            print(f"StaleElementReferenceException {i}: {e}")
            continue 
       
#     # Move to next page btn and click
#     action.move_to_element(next_page_btn).perform
#     time.sleep(2)
#     next_page_btn.click()
#     # time.sleep(0.2)  
#     # saved_jobs = 0

   
    # # Move to next page btn and click until last page
    # action.move_to_element(next_page_btn).perform
    # time.sleep(2)
    # next_page_btn.click()
    # time.sleep(0.2)
    # try:
    #     disabled_next_page_btn = driver.find_element(By.XPATH, '//li[@class="pagination-next page-item ng-star-inserted disabled"]')
    #     break        
    # except NoSuchElementException:
    #     pass
    # saved_jobs = 0
