from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from Functionality.functions import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# driver = webdriver.Chrome(options=options)
driver = webdriver.Chrome()
    # Fullscrin browser
driver.maximize_window()
# Open dice
driver.get("https://www.dice.com/dashboard/login")

# login, input email and than next page is password input
wait_element(driver, '//input[@type="email"]')
input_keys(driver, '//input[@type="email"]', "stan.hordon@gmail.com")
random_sleep(0.1, 3)
click(driver, '//button[@type="submit"]')
wait_element(driver, '//input[@placeholder="Enter Password"]')
input_keys(driver, '//input[@placeholder="Enter Password"]', "skaya2301")
wait_element(driver,'//dhi-seds-nav-footer')
click(driver, '//button[@data-testid="submit-password"]')
submit_search_button = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH,'//button[@id="submitSearch-button"]')))

# searching for job possition by filters
input_keys(driver, '//input[@id="typeaheadInput"]', "Software QA")
submit_search_button.click()

time.sleep(35)