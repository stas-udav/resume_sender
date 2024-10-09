from unittest import result
from webbrowser import Chrome
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import json
import datetime
import imaplib
import email
from email.header import decode_header
import quopri
from bs4 import BeautifulSoup
import re
import string
import random

from trio import sleep_until

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
        # If duplicate in existing_jobs skipped and moving forward
        if key not in existing_jobs:
            # If this key not exist in file we add in new dict
            existing_jobs[job_title] = company_name, today_date()
    
    # Save data in file    
    with open(filename, 'w') as f:
        #indent=4: Этот аргумент указывает на отступ в
            #4 пробела для удобочитаемости выходного JSON-файла.
        json.dump(existing_jobs, f, indent=4) 

# Pull cookies from txt
def load_cookies(filename):
    try:
        with open(filename, 'r') as file:
            cookies = json.load(file)
            return cookies
    except FileNotFoundError:
        print("ERROR - NO COOKIE")
        return None

# Send keys to input field
def input_keys(driver, xpath, input_keys):    
    input_field = driver.find_element(By.XPATH, xpath)
    input_field.send_keys(input_keys)
    random_sleep(0.1, 3)
 
def click(driver, xpath):
    target = driver.find_element(By.XPATH, xpath)
    target.click()

# Read email in gmail
def gmail_read(imap_server, imap_user_email, imap_password, email_subject):
    # Connecting to IMAP server and creating object IMAP4_SSL
    mail = imaplib.IMAP4_SSL(imap_server)
    mail.login(imap_user_email, imap_password)
    # Search for email in inbox folder by subject
    mail.select("INBOX")
    result, data = mail.search(None,f'(UNSEEN SUBJECT "{email_subject}")')
    
    if result == 'OK':
        # Construct a list of unique email identifiers from the fetched information
        email_ids = data[0].split()
        # Check if we have unread e-mail with subject
        if email_ids:
            # Reciving last email id(new email)
            # print("Email IDs:", email_ids)
            latest_email_id = email_ids[-1]
            _, email_data = mail.fetch(latest_email_id, "(RFC822)")
            raw_email = email_data[0][1]
            # print("Raw Email:", raw_email)
            # Reciving  email_message data [0] - The original contents of the email,
            # a raw text copy of the email received directly from the IMAP server.
            # data[1] - he second element must contain the contents of the letter itself in the form of bytes
            email_message = email.message_from_bytes(raw_email)
            # print("Email Message:", email_message)

            # Getting text from email
            for part_email in email_message.walk():
                if part_email.get_content_type() == "text/html":
                    # Decode from bites to line 
                    email_message_body = part_email.get_payload(decode=True).decode()
                    # Extracting text from html
                    text_email_message = extract_text_from_html(email_message_body)
                    # print(text_email_message)
                    code = extract_indeed_code(text_email_message)
                    print(code)
                    # Mark the email as deleted
                    mail.store(latest_email_id, '+FLAGS', '\\Deleted')
                    # Permanently remove deleted emails
                    mail.expunge()
                    return code
            
def extract_text_from_html(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    text = soup.get_text()
    return text

def extract_indeed_code(email_message_body):
    # Searching for line with autorization code
    match = re.search(r'Use this six digit code to sign in to your Indeed account:\s*\n*\s*(\d{6})', email_message_body)
    if match:
            code = match.group(1)  # Извлекаем шестизначный код
            return code
    else:
        return None
    

# Generate random right part of email
def email_randomize(email):
    # separate left and right part of email
    email_parts = email.split("@")
    user_part_email = email_parts[0]
    domain_part_email = email_parts[1]
    # generate random str for user_part of email
    random_symbols = ""
    for _ in range(5):
        random_symbol = random.choice(string.ascii_lowercase)
        random_symbols += random_symbol
               
    modified_email = user_part_email + "+" + random_symbols + "@" + domain_part_email
    print(modified_email)
    return modified_email

def wait_element(driver, xpath):
    wait = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, xpath)))
    return wait

def wait_elements(driver, xpath):
    wait = WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))
    return wait

# random sleep time
def random_sleep(min_sec, max_second):
    time.sleep(random.uniform(min_sec, max_second))
    

