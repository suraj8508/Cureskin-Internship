"""
Find the bugs and fix this script with Python and Selenium

Write different locators for the search bar and the button

The following import can't be used:
from selenium.webdriver.common.keys import Keys

Test case:
    Open google.com
    Search for Python
    Verify Python is on the results
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(executable_path="/Users/sbt/Documents/automation/Cureskin-Internship/chromedriver_new/chromedriver")
url = "https://www.google.com"

browser.get(url)
search_query = "python"
search_bar = browser.find_element(By.ID, 'APjFqb')
search_bar.clear()
ActionChains(browser).move_to_element(search_bar).send_keys(search_query).perform()

browser.wait = WebDriverWait(browser, 10)
search_btn = browser.find_element(By.NAME, "btnK")
browser.wait.until(EC.element_to_be_clickable(search_btn)).click()

assert search_query in browser.current_url, f"Search query {search_query} not in {browser.current_url}"
print("Test case passed")

browser.quit()




