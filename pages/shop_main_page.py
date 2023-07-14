from pages.base_page import Page
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class MainPage(Page):
    POP_UP_X = (By.CSS_SELECTOR, 'button.popup-close')

    def open_main_page(self):
        self.open_url()
        self.click(*self.POP_UP_X)
