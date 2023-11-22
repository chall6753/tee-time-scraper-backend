from selenium import webdriver
from selenium.webdriver.common.by import By
from functions.utils import startBrowser

from dotenv import load_dotenv
import os
import time

def login():
    load_dotenv()
    email = os.getenv('email')
    password = os.getenv('password')
    
    driver = startBrowser()

    time.sleep(10)

    # # click login
    driver.find_element(By.ID,"login").click()

    time.sleep(5)
    
    
    # find the username field
    driver.find_element(By.ID, "mat-input-1").click()
    emailElement = driver.find_element(By.ID, "mat-input-1")
    for char in email:
        emailElement.send_keys(char)
        time.sleep(.3)
    
    time.sleep(5)

    # find password input field and input password
    driver.find_element(By.ID, "mat-input-2")
    passwordElement = driver.find_element(By.ID, "mat-input-2")
    for char in password:
        passwordElement.send_keys(char)
        time.sleep(.3)

    time.sleep(5)

    # Switch to ifram window
    iframe = driver.find_element(By.XPATH, "//*[@id='ngrecaptcha-0']/div/div/iframe")
    driver.switch_to.frame(iframe)

    time.sleep(5)
    
    #click on captcha
    driver.find_element(By.ID, "recaptcha-anchor").click()

    time.sleep(5)
    
    driver.switch_to.default_content()

    time.sleep(5)

    # # click on submit
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


    while(True):
        pass
     

