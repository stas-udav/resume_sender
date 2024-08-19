from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time
from Functionality.functions import wait_element, input_keys, random_sleep, wait_elements
from Functionality.functions import click

from selenium.webdriver.support import expected_conditions as EC

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

# Checking pop up
if wait_element(driver, '//div[@class="fe-popup70 fe-popup130"]'):    
    driver.find_element(By.XPATH, '//div[@class="fe-popup-cross"]').click()       
else:    
    pass

time.sleep(2)

# Searching for job possition by filters
location_btn = driver.find_element(By.XPATH,'//button[@id="IPGeoLocateButton"]')
action.move_to_element(location_btn).perform()
time.sleep(0.2)
input_keys(driver, '//input[@id="typeaheadInput"]', "Software QA")
random_sleep(0.1, 3)
submit_search_button = driver.find_element(By.XPATH, '//button[@id="submitSearch-button"]')
submit_search_button.click()
random_sleep(1, 3)

# Going up to the parent element and extracting text from it 
# work_type = 'Remote'
# posted_date = 'Last 3 Days'
# easy_apply = 'Yes'
# work_setting = wait_element(driver, f"//div[@id='searchFacetsDesktop']//*[normalize-space(text())= '{work_type}']") # * - any element with text
# # action.move_to_element(work_setting).perform()
# work_setting.click()
# date_p = wait_element(driver, f"//div[@id='searchFacetsDesktop']//*[normalize-space(text())= '{posted_date}']")
# date_p.click()
# easy_a = wait_element(driver, f"//div[@id='searchFacetsDesktop']//*[normalize-space(text())= '{easy_apply}']")
# easy_a.click()
work_setting = ['Remote', 'Last 3 Days', 'Yes']
for filter in work_setting:
    set_element = wait_element(driver, f"//div[@id='searchFacetsDesktop']//*[normalize-space(text())= '{filter}']")
    time.sleep(0.2)  # Добавляем небольшую задержку
    set_element.click()
    time.sleep(0.1)

# Going through jobs, click on them and save date, apply
# next_page_disbled = wait_element(driver, '//li[@class="pagination-next page-item ng-star-inserted disabled"]')

next_page_btn = wait_element(driver, '//li[@class="pagination-next page-item ng-star-inserted"]')
while next_page_btn:
    jobs = wait_elements(driver, '//div[@class="card search-card"]')
    print(len(jobs))
    saved_jobs = 0

    for job in jobs: 
        # check if amount of grabbed jobs equals jobs on page
        time.sleep(3)
        if saved_jobs < len(jobs):        
            job.click()
            time.sleep(10)        
            saved_jobs +=1
            print(saved_jobs)