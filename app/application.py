from pages.shop_main_page import MainPage
from pages.header_page import Header
from pages.search_result_page import SearchResults


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.shop_main_page = MainPage(self.driver)
        self.header_page = Header(self.driver)
        self.search_result_page = SearchResults(self.driver)


