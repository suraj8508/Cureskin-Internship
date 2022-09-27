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

    FOOTER_HEADING = (By.CSS_SELECTOR, 'div.footer div.col span.widget-title')
    FOOTER_PROD = (By.CSS_SELECTOR, 'div.footer-widgets.footer div.row div.col')
    FOOTER_BEST_PROD = (By.CSS_SELECTOR, 'div#woocommerce_products-11')
    FOOTER_LATEST_PROD = (By.CSS_SELECTOR, 'div#woocommerce_products-12')
    FOOTER_TOP_PROD = (By.CSS_SELECTOR,'div#woocommerce_top_rated_products-3')
    FOOTER_PROD_TITLES = (By.CSS_SELECTOR, 'div.footer div.col ul.product_list_widget span.product-title')
    FOOTER_PROD_PRICES = (By.CSS_SELECTOR, 'div.footer div.col ul.product_list_widget span.amount')
    FOOTER_PROD_STAR = (By.CSS_SELECTOR, 'div.footer div.col div.star-rating span[style="width:100%"]')
    FOOTER_COPYRIGHTS =(By.CSS_SELECTOR, 'div.dark div.container div.footer-primary div.copyright-footer')
    FOOTER_LAPTOP = (By.CSS_SELECTOR, 'div.menu-laptop-container li.menu-item a[href*="product-category/laptop/"]')
    FOOTER_TABLET = (By.CSS_SELECTOR, 'div.menu-laptop-container li.menu-item a[href*="product-category/tablet/"]')
    FOOTER_PHONE = (By.CSS_SELECTOR, 'div.menu-laptop-container li.menu-item a[href*="product-category/phone/"]')
    FOOTER_ACCESSORIES = (By.CSS_SELECTOR, 'div.menu-laptop-container li.menu-item a[href*="product-category/accessories/"]')
    FOOTER_BK2TP_BTN = (By.XPATH, '//*[@id="top-link"]')




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

    def footer_category_visible(self):
        footer_category = self.find_elements(*self.FOOTER_HEADING)

        for i in range(len(footer_category)):
            footer_category[i].is_displayed()
            sleep(2)

    def verify_prod_title_name_star(self):
        footer_all_prod = self.find_elements(*self.FOOTER_PROD)

        for i in range(len(footer_all_prod)):
            self.verify_best_prod()
            self.verify_latest_prod()
            self.verify_top_prod()

    def verify_best_prod(self):
        best_prod = self.find_elements(*self.FOOTER_BEST_PROD)
        footer_prod_price = self.find_element(*self.FOOTER_PROD_PRICES)
        footer_prod_star = self.find_element(*self.FOOTER_PROD_STAR)
        footer_prod_title = self.find_element(*self.FOOTER_PROD_TITLES)
        for i in range(len(best_prod)):
            print(footer_prod_price.is_displayed())
            print(footer_prod_title.is_displayed())
            print(footer_prod_star.is_displayed())

    def verify_latest_prod(self):
        best_prod = self.find_elements(*self.FOOTER_LATEST_PROD)
        footer_prod_price = self.find_element(*self.FOOTER_PROD_PRICES)
        footer_prod_star = self.find_element(*self.FOOTER_PROD_STAR)
        footer_prod_title = self.find_element(*self.FOOTER_PROD_TITLES)
        for i in range(len(best_prod)):
            print(footer_prod_price.is_displayed())
            print(footer_prod_title.is_displayed())
            print(footer_prod_star.is_displayed())

    def verify_top_prod(self):
        best_prod = self.find_elements(*self.FOOTER_TOP_PROD)
        footer_prod_price = self.find_element(*self.FOOTER_PROD_PRICES)
        footer_prod_star = self.find_element(*self.FOOTER_PROD_STAR)
        footer_prod_title = self.find_element(*self.FOOTER_PROD_TITLES)
        for i in range(len(best_prod)):
            print(footer_prod_price.is_displayed())
            print(footer_prod_title.is_displayed())
            print(footer_prod_star.is_displayed())

    def copyright_sign_visible(self):
        copyright_sign = self.find_element(*self.FOOTER_COPYRIGHTS)
        print(copyright_sign.is_displayed())

    def footer_btn_top(self):
        footer_bk_btn = self.wait_for_element_appear(*self.FOOTER_BK2TP_BTN)
        print(footer_bk_btn.is_displayed())

    def verify_prod_category_links(self):
        self.verify_category_laptop_opened()
        self.verify_category_tablet_opened()
        self.verify_category_phones_opened()
        self.verify_category_accessories_opened()

    def verify_category_laptop_opened(self):
        link_lap_category = self.find_element(*self.FOOTER_LAPTOP)
        link_lap_category.click()
        self.verify_url_contains_query('product-category/laptop/')

    def verify_category_tablet_opened(self):
        link_tab_category = self.find_element(*self.FOOTER_TABLET)
        link_tab_category.click()
        self.verify_url_contains_query('product-category/tablet/')

    def verify_category_phones_opened(self):
        link_ph_category = self.find_element(*self.FOOTER_PHONE)
        link_ph_category.click()
        self.verify_url_contains_query('product-category/phone/')

    def verify_category_accessories_opened(self):
        link_acc_category = self.find_element(*self.FOOTER_ACCESSORIES)
        link_acc_category.click()
        self.verify_url_contains_query('product-category/accessories/')
