from urllib import response
import cloudscraper
import cfscrape
from bs4 import BeautifulSoup
import pandas as pd
from requests_toolbelt import user_agent
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from playwright.sync_api import sync_playwright
import time

# def scrape_jobs():
#     base_url = "https://www.indeed.com/jobs?q=software+qa+engineer&fromage=3&vjk=562853c172cdc4e0"
#     scraper = cloudscraper.create_scraper()
#     headers =  {
#     "authority": "t.indeed.com",
#     "method": "POST",
#     "path": "/signals/gnav/log?from=jobsearch~indeedmobile-serpglobal&parentLogId=1iblt65e7jdkq801&hostAppTk=1iblt65scj5528aa",
#     "scheme": "https",
#     "accept": "*/*",
#     "accept-encoding": "gzip, deflate, br, zstd",
#     "accept-language": "en-US,en;q=0.9",
#     "cache-control": "no-cache",
#     "content-length": "126",
#     "content-type": "text/plain;charset=UTF-8",
#     "cookie": "CTK=1hqh4o7u5imqh801; SURF=...",
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
#     }

#     response = scraper.get(base_url, headers=headers)
#     print(response.status_code)
#     bs = BeautifulSoup(response.content, "html.parser")
#     print(bs.prettify())

# driver = webdriver.Chrome()
# driver.maximize_window()

# possition = "software+qa+engineer"
# posting_date = "3" # Value 1, 3, 7, 14

# driver.get(f"https://www.indeed.com/jobs?q={possition}&fromage={posting_date}")


# if __name__ == "__main__":
#     scrape_jobs()

# driver = webdriver.Chrome()
# possition = "software+qa+engineer"
# posting_date = "3"
# # driver.get("https://www.indeed.com/jobs?q=software+qa+engineer&fromage=3&vjk=562853c172cdc4e0")
# with sync_playwright() as pl:
#     browser = pl.chromium.launch(headless=False)
#     context = browser.new_context(user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36')
#     page = context.new_page()
#     page.goto("https://www.indeed.com/jobs?q=software+qa+engineer&l=&from=searchOnDesktopSerp&vjk=670c3e2a67d2e4b0")
#     time.sleep(4)
#     last_height = page.evaluate("document.body.scrollHeight")
    
#     while True:
#         page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
#         time.sleep(2)
#         page.wait_for_timeout(1000)
#         new_height = page.evaluate("document.body.scrollHeight")

#         if new_height == last_height:
#             break
#         last_height = new_height

#     content = page.content()
#     bs = BeautifulSoup(content, "html.parser")
#     # print(bs.prettify())

#     with open ("content.html", "w", encoding="utf-8") as f:
#         f.write(content)

url = "https://www.indeed.com/jobs?q=software+qa+engineer&fromage=3&vjk=562853c172cdc4e0"
scraper = cloudscraper.create_scraper()
res = scraper.get(url)
print(res.status_code)
response = res.text
print(response)
# time.sleep(5)
# scrape = cfscrape.create_scraper()
# res1 =  scrape.get(url)
# print(res1.status_code)