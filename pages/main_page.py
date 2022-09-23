from pages.base_page import Page
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select

class MainPage(Page):
    TOPBNR_RIGHT_ARW = (By.CSS_SELECTOR, 'button.next[type="button"][aria-label="Next"]')
    RIGHT_CLK_IMG = (By.CSS_SELECTOR, 'div.banner-layers.container a[href*="/samsung-galaxy-chromebook"]')
    TOPBNR_LEFT_ARW = (By.CSS_SELECTOR, 'button.previous[type="button"][aria-label="Previous"]')
    LEFT_CLK_IMG = (By.CSS_SELECTOR, 'div.banner-layers.container a[href*="/xiaomi-11t-pro/"]')

    def open_main(self):
        self.open_url()

    def click_right_arw(self):
        right_arw = self.find_element(*self.TOPBNR_RIGHT_ARW)
        actions = ActionChains(self.driver)
        actions.move_to_element(right_arw)
        actions.click(right_arw)
        actions.perform()
        sleep(2)
        img_display = self.find_element(*self.RIGHT_CLK_IMG)
        print(img_display.is_displayed())

    def click_left_arw(self):
        left_arw = self.find_element(*self.TOPBNR_LEFT_ARW)
        actions = ActionChains(self.driver)
        actions.move_to_element(left_arw)
        actions.click(left_arw)
        actions.perform()
        sleep(2)
        img_display = self.find_element(*self.RIGHT_CLK_IMG)
        print(img_display.is_displayed())
