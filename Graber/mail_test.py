#! /usr/bin/env python3
from pydoc import cli
from Config.indeed_config import *
from Functionality.functions import *
# from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import undetected_chromedriver as webdriver

import os
import time
import random

# opneт profile

# email = email_randomize("stan.se.gordon@gmail.com")

# gmail_read("imap.gmail.com", "stan.se.gordon@gmail.com", "kzne wtez kfmq kuxd", "Indeed one-time passcode")   

# Create a new browser instance 
    # turn off google security login check
options = webdriver.ChromeOptions()
options.binary_location = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
# options.add_argument('disable-infobars')
# options.add_argument('--safebrowsing-disable-extension-blacklist')
# options.add_argument('--safebrowsing-disble-download-pritection')
# options.add_argument('--disable-site-isolation-trials')
profile = "C:\\Users\\stanh\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 3"
options.add_argument(f"user-data-dir={profile}")
#     # Setup
driver = webdriver.Chrome(options=options)
# driver = webdriver.Chrome()
    # Fullscrin browser
driver.maximize_window()
# Выполнение JavaScript для открытия новой вкладки
driver.execute_script("window.open('');")

# Переключение на новую вкладку
driver.switch_to.window(driver.window_handles[-1])

# Открытие URL в новой вкладке
driver.get("https://www.google.com")
# driver.get("https://www.google.com/") 
# time.sleep(2)
# click(driver, '//span[@class="gb_Kd"]')
# time.sleep(2)
# input_keys(driver,'//input[@type="email"]', 'stan.se.gordon@gmail.com')
# time.sleep(2)
# click(driver, '//button[@class="VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-dgl2Hf nCP5yc AjY5Oe DuMIQc LQeN7 BqKGqe Jskylb TrZEUc lw1w4b"]')


# loggin into indeed accaunt utilizing temporary code from gmail 
driver.get("https://indeed.com")
time.sleep(random.uniform(1,7))
click(driver, '//a[@class="css-ng3gx5 e19afand0"]')
time.sleep(random.uniform(1,7))
# driver.get("https://secure.indeed.com/auth?hl=en_US&co=US&continue=https%3A%2F%2Fwww.indeed.com%2F%3Ffrom%3Dgnav-homepage&tmpl=desktop&from=gnav-util-homepage&jsContinue=https%3A%2F%2Fonboarding.indeed.com%2Fonboarding%3Fhl%3Den_US%26co%3DUS%26from%3Dgnav-homepage&empContinue=https%3A%2F%2Faccount.indeed.com%2Fmyaccess")
wait_loading_page(driver, 5, '//footer[@class="icl-GlobalFooter"]')

# email_changed = email_randomize("stan.se.gordon@gmail.com")
input_keys(driver, '//input[@name="__email"]', "stan.se.gordon@gmail.com")
wait_loading_page(driver,3, '//button[@type="submit"]')
# indeed_google_login_button = driver.find_element(By.XPATH '//button[@id="login-google-button"]')
time.sleep(random.uniform(1,7))
click(driver, '//button[@type="submit"]')
# click(driver, '//button[@id="login-google-button"]')
time.sleep(random.uniform(1,7))
sing_in_button = driver.find_element(By.XPATH, '//a[text() = "Sign in with login code instead"]')
# sing_in_button_text = sing_in_button.text
# print(sing_in_button_text)
click(driver, sing_in_button)
# driver.execute_script("arguments[0]:",sing_in_button)
# click(driver, '//button[@id="gsuite-login-google-button"]')
time.sleep(random.uniform(1,7))
# getting autorization code from e-mail and paste into passcode input field
code = gmail_read("imap.gmail.com", "stan.se.gordon@gmail.com", "kzne wtez kfmq kuxd", "Indeed one-time passcode")
input_keys(driver, '//input[@id="passcode-input"]', code)
time.sleep(random.uniform(1,7))
click(driver, '//button[@data-tn-element="otp-verify-login-submit-button"]')
wait_loading_page(driver,3, '//button[@type="submit"]')