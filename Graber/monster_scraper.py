from urllib import response
import cloudscraper
import cfscrape
import time
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.linkedin.com/jobs/search/?currentJobId=4064896579&distance=25&geoId=103644278&keywords=quality%20assurance&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true"
# scraper = cloudscraper.create_scraper()
# res = scraper.get(url)
# print(res.status_code)
# response = res.text
# print(response)
# time.sleep(5)
scrape = cfscrape.create_scraper()
res1 =  scrape.get(url)
print(res1.status_code)
response1 = res1.text
# print(response1)

bs = BeautifulSoup(response1, 'html.parser')

print(bs.prettify())