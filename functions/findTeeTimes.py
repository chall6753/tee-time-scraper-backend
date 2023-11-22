from selenium import webdriver
from selenium.webdriver.common.by import By
from functions.utils import startBrowser

from dotenv import load_dotenv
import os
import time

def findTeeTimes(driver):

    year = '2023'
    month = 'November'
    day = '23'
    selectYear = f'button[aria-label="{year}"]'
    selectMonth = f'button[aria-label="{month} {year}"]'
    selectDay = f'button[aria-label="{month} {day}, {year}"]'


    driver.find_element(By.CSS_SELECTOR, "button[aria-label='Open calendar']").click()
    driver.find_element(By.CSS_SELECTOR, "button[aria-label='Choose month and year']").click()
    driver.find_element(By.CSS_SELECTOR, selectYear).click()
    driver.find_element(By.CSS_SELECTOR, selectMonth).click()
    time.sleep(3)
    driver.find_element(By.CSS_SELECTOR, selectDay).click()
    time.sleep(3)
    teeTimeElements = driver.find_elements(By.CSS_SELECTOR, "div[class='time']")
    courses = driver.find_elements(By.CSS_SELECTOR, "div[class='time] > div")

    print(courses)

    teeTimes = []
    for teeTime in teeTimeElements:
        
        # x = driver.find_elements(By.CSS_SELECTOR, "div[class='time']").text()
        # print(x)
        teeTimes.append(teeTime.text)

    # print(teeTimes)