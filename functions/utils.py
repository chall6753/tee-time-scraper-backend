from selenium import webdriver
from selenium.webdriver.common.by import By

from dotenv import load_dotenv
import os
import time

def startBrowser():
    load_dotenv()
    url  = os.getenv('url')
    path = "C:\\Users\\chall\\chromedriver-win64\\chromedriver.exe"
     
    # giving the path of chromedriver to selenium webdriver
    driver = webdriver.Chrome()
     
    # # opening the website  in chrome.
    driver.get(url)

    

    return driver