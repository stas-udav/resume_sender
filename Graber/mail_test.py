#! /usr/bin/env python3
from pydoc import cli
from Config.indeed_config import *
from Functionality.functions import *
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException

import os
import time
import random

# opne profile

email = email_randomize("stan.se.gordon@gmail.com")

# gmail_read("imap.gmail.com", "stan.se.gordon@gmail.com", "kzne wtez kfmq kuxd", "Indeed one-time passcode")   