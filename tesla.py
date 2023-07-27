from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/Users/sbt/Documents/automation/Cureskin-Internship/chromedriver_new/chromedriver")
SIDE_SCROLLER = driver.find_element(By.CSS_SELECTOR, '#block-tesla-frontend-content div.tcl-homepage-content-snapping')
MOD_INVN = driver.find_elements(By.CSS_SELECTOR, 'p.tds-colorscheme--light a[href="/inventory/new/mx"].tds-link')

url = "https://www.tesla.com/"
driver.get(url)
driver.maximize_window()
sleep(2)
# driver.execute_script("window.scrollBy(0, 1000)", "")     # Scroll by Pixel
driver.execute_script("arguments[0]. scrollIntoView();", MOD_INVN)     # Scroll to element
driver.execute_script("windows.scrollBy(0, document.body.scrollHeight)")    # Scroll to the end of page
sleep(3)



# search_query = "Python"
# search_bar = driver.find_element(By.CSS_SELECTOR, 'input#searchInput')
# search_bar.clear()
# search_bar.send_keys(search_query)
# search_icon = driver.find_element(By.CSS_SELECTOR, 'button.pure-button').click()
# # curr_url =
#
# assert search_query in driver.current_url, f"Search query {search_query} not in {driver.current_url}"
# print("Test case passed")

driver.quit()

