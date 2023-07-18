from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

url = "https://www.wikipedia.org/"

driver = webdriver.Chrome(executable_path="/Users/sbt/Documents/automation/Cureskin-Internship/chromedriver")

driver.get(url)
search_query = "Python"
search_bar = driver.find_element(By.CSS_SELECTOR, 'input#searchInput')
search_bar.clear()
search_bar.send_keys(search_query)
search_icon = driver.find_element(By.CSS_SELECTOR, 'button.pure-button').click()
# curr_url =

assert search_query in driver.current_url, f"Search query {search_query} not in {driver.current_url}"
print("Test case passed")

driver.quit()

