from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
import os
import time

EMAIl = os.environ["Email"]
PASSWORD = os.environ["Password"]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3962661047&f_"
           "AL=true&geoId=105214831&keywords=python%20developer&location=Bengaluru"
           "%2C%20Karnataka%2C%20India&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true")

signin = driver.find_element(By.CLASS_NAME, value="btn-secondary-emphasis")
signin.click()

time.sleep(2)

email = driver.find_element(By.ID, value="username")
email.send_keys(EMAIl)

password = driver.find_element(By.ID, value="password")
password.send_keys(PASSWORD)

enter = driver.find_element(By.CLASS_NAME, value="from__button--floating")
enter.click()

# Applying for Job

# ---- To be continued
