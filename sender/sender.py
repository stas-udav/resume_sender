from email.policy import strict
from re import split
from numpy import append
import pandas as pd
import openpyxl
import pprintpp
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from Functionality.functions import *
import pprint
import time

    # Create a new browser instance 
    # Setup
# driver = webdriver.Chrome()
# #     # Fullscrin browser
# driver.maximize_window() 

# Waiting for the page to load
# wait_loading_page(driver, 5,'//footer[@class="icl-GlobalFooter"]')

# Load spreadsheet
xl = pd.ExcelFile('output1.xlsx')
# print(xl)
# # Load a sheet into a DataFrame
df = xl.parse(xl.sheet_names[0])

# Ensure your columns don't contain any NaNs
df.dropna(inplace=True)

jobs = dict(df)
# print(type(str(jobs["stas"])))
# print(jobs)
str_job = str(jobs["stas"])
j = str_job.split(" ")
links = []     

for i in range(4, len(j), 4):
    links.append(j[i])


print(links) 
