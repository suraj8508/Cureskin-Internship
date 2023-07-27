from pages.base_page import Page
from time import sleep
from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.support.ui import Select


class SearchResults(Page):
    PRODUCT_COUNT = (By.ID, 'ProductCount')

    def verify_search_results(self, expected_text):
        sleep(2)
        self.verify_partial_text(expected_text, *self.PRODUCT_COUNT)




