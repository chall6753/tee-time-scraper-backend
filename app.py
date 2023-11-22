from functions.login import login
from functions.findTeeTimes import findTeeTimes
from functions.utils import startBrowser

driver = startBrowser()

findTeeTimes(driver)

while(True):
    pass