from pages.base_page import Page
from selenium.webdriver.common.by import By


class MainPage(Page):
    def open_main(self):
        self.open_url()


