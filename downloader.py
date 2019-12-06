from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import os

from time import sleep

ACCOUNT_NAMES = [ 
        "RER_A", 
        "RERB", 
        "RERC_SNCF", 
        "RERD_SNCF", 
        "Ligne1_RATP", 
        "Ligne2_RATP", 
        "Ligne3_RATP", 
        "Ligne4_RATP", 
        "Ligne5_RATP", 
        "Ligne6_RATP", 
        "Ligne7_RATP", 
        "Ligne8_RATP", 
        "Ligne9_RATP", 
        "Ligne10_RATP", 
        "Ligne11_RATP", 
        "Ligne12_RATP", 
        "Ligne13_RATP", 
        "Ligne14_RATP", 
        "T1_RATP", 
        "T2_RATP", 
        "T3a_RATP", 
        "T3b_RATP", 
        "T6_RATP", 
        "T7_RATP", 
        "T8_RATP", 
]

# You need to adapt it according to
# your network speed and CPU
PAUSE_TIME = 1.5

if not os.path.exists("pages"):
    os.makedirs("pages")

with webdriver.Firefox() as driver:
    for account in ACCOUNT_NAMES:
        driver.get(f"https://twitter.com/{account}?lang=fr")
        
        # Get scroll height
        last_height = driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

            # Wait to load page
            sleep(PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        with open(f"pages/{account}.html", 'w') as f:
            f.write(driver.page_source)

    driver.quit()
