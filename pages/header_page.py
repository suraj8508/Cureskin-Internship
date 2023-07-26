from pages.base_page import Page
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class Header(Page):
    HEADER_SEARCH = (By.CSS_SELECTOR, 'search-modal.header__search summary.header__icon span')
    MOB_HEAD_SEARCH = (By.XPATH, '//*[@id="shopify-section-header"]/sticky-header/header/div/search-modal/details/summary/span/svg[1]')
    SEARCH_BAR = (By.ID, 'Search-In-Modal')
    CLICK_SEARCH = (By.CSS_SELECTOR, '#predictive-search-option-search-keywords button.button')

    def open_search_bar(self):
        self.wait_for_element_click(*self.HEADER_SEARCH)

    def open_search_bar_m(self):
        # self.find_elements(*self.HEADER_SEARCH)
        self.wait_for_element_click(*self.MOB_HEAD_SEARCH)

    def insert_search_word(self, search_word):
        self.input_text(search_word, *self.SEARCH_BAR)
        self.wait_for_element_click(*self.CLICK_SEARCH)

