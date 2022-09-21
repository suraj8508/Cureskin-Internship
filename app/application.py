from pages.main_page import MainPage
from pages.header_page import Header


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.main_page = MainPage(self.driver)
        self.header_page = Header(self.driver)
