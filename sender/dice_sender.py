from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from Functionality.functions import wait_element, input_keys, random_sleep, wait_elements
from Functionality.functions import click
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
    # Fullscrin browser
driver.maximize_window()
# Open dice
driver.get("https://www.dice.com/dashboard/login")

# Login, input email and than next page is password input
wait_element(driver, '//input[@type="email"]')
input_keys(driver, '//input[@type="email"]', "stan.hordon@gmail.com")
random_sleep(0.1, 3)
click(driver, '//button[@type="submit"]')
wait_element(driver, '//input[@placeholder="Enter Password"]')
input_keys(driver, '//input[@placeholder="Enter Password"]', "skaya2301")
random_sleep(0.1, 3)
wait_element(driver,'//dhi-seds-nav-footer')
click(driver, '//button[@data-testid="submit-password"]')
submit_search_button = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH,'//button[@id="submitSearch-button"]')))

# Searching for job possition by filters
input_keys(driver, '//input[@id="typeaheadInput"]', "Software QA")
random_sleep(0.1, 3)
submit_search_button.click()
random_sleep(1, 3)
check_boxes = wait_elements(driver, "//button[@role='checkbox']")
# Going up to the parent element and extracting text from it 
for checkbox in check_boxes:
    checkbox = checkbox.find_element(By.XPATH, '..')    
    checkbox_text = checkbox.text
    # print(checkbox_text)
    if 'Remote' in checkbox_text:
        checkbox.click()
        print(f'Click on {checkbox.text}')
        random_sleep(0.1, 3)
    # Time when job was posted
    random_sleep(0.1, 3)
    time_frame = 'Today'
    posted_date = wait_element(driver, f"//button[normalize-space(text())='{time_frame}']")
    posted_date.click()
    print(posted_date.text)
    random_sleep(0.1, 3)
    if 'Yes' in checkbox_text: #//dhi-accordion/div/div[text()='Easy Apply']
        checkbox.click()
        random_sleep(0.1, 3)
        print(f'Click on {checkbox.text}')


time.sleep(35)