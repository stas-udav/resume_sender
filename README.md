# resume_sender
This script automates the process of logging into Dice.com, searching for job listings, applying filters, and applying to each job. The script is built using Python and Selenium.

Requirements:
Python 3.12.0
pip install requirements.txt

Usage:
folder resume_sender\sender
1. run dice_sender.py
2. Login: A login prompt will appear. Enter your Dice credentials.

Job Search and Application:
The script opens the job search page and applies filters specified in the work_setting list.
It iterates over job listings and attempts to apply to each one with Easy apply possibilities.
Job IDs are stored in jobs_dice.json to prevent duplicate applications, file will be created by script and will use all next iterations

Code Structure
Login Automation: Uses Tkinter for GUI login prompt.
Job Search: Filters job results and loads more pages.
Application Process: Opens each job, applies, and saves data to JSON.
Error Handling
The script handles common exceptions:

Timeouts: Skips failed elements.
Stale Elements: Retries when encountering stale references.
External URLs: Ignores links that don’t match Dice’s domain.
Notes
Customize work_setting filters based on your search criteria.
