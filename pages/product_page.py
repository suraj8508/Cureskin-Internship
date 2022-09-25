from pages.base_page import Page
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select


class ProductPage(Page):
    expected_text = ''
    PROD_IMAGE = (By.CSS_SELECTOR, 'div.box-image img.attachment-woocommerce_thumbnail')
    WISHLIST_ICON = (By.CSS_SELECTOR, 'div.wishlist-icon i.icon-heart')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.box-text div.title-wrapper p.name a')
    WISHLIST_PROD_NAME = (By.CSS_SELECTOR, 'table.cart td.product-name a')
    WISHLIST_REMOVE =(By.CSS_SELECTOR, 'table.cart td.product-remove a')
    MSG_CONFIRM = (By.CSS_SELECTOR, 'div.woocommerce-message div.container.container')
    WISHLIST_SOCIAL =(By.CSS_SELECTOR, 'div.yith_wcwl_wishlist_footer div.social-icons a')

    SORT_BOX = (By.CSS_SELECTOR, '.orderby')
    PAGINATION = (By.CSS_SELECTOR, 'div.container nav.woocommerce-pagination ul.links li')

    PRICE_FILTER_SLIDER = (By.CSS_SELECTOR, 'span[style="left: 100%;"]')
    FILTER_BTN = (By.CSS_SELECTOR, 'div.price_slider_amount button.button')
    FILTER_RESULT_MSG = (By.CSS_SELECTOR, 'main#main div.shop-container p.woocommerce-info')
    PRICE_FILTER_SLIDER2 = (By.XPATH, '//*[@id="woocommerce_price_filter-9"]/form/div/div[1]/span[2]')

    def open_lap_category_page(self):
        self.open_url('product-category/laptop/')

    def open_access_category_page(self):
        self.open_url('product-category/accessories/')

    def open_phn_category_page(self):
        self.open_url('product-category/phone/')

    def open_whole_prod_page(self):
        self.open_url('shop/')

    def open_sort_popular_page(self):
        self.open_url('shop/?orderby=popularity')

    def add_prod_wishlist(self):
        self.hover_to_prod_img()
        wish_icon = self.find_element(*self.WISHLIST_ICON)
        actions = ActionChains(self.driver)
        actions.move_to_element(wish_icon)
        actions.click(wish_icon)
        actions.perform()
        sleep(1)

    def hover_to_prod_img(self):
        prod_img = self.find_element(*self.PROD_IMAGE)
        actions = ActionChains(self.driver)
        actions.move_to_element(prod_img)
        actions.perform()

    def open_wishlist_page(self):
        self.expected_text = self.find_element(*self.PRODUCT_NAME).text
        self.hover_to_prod_img()
        wish_icon = self.find_element(*self.WISHLIST_ICON)
        actions = ActionChains(self.driver)
        actions.move_to_element(wish_icon)
        actions.double_click(wish_icon)
        actions.perform()
        # sleep(2)

    def verify_prod_in_wishlist(self):
        all_products = self.find_elements(*self.PRODUCT_NAME)
        # expected_text = 'ASUS Chromebook Flip C434 2-In-1'
        # for title in range(len(all_products)):
        #     expected_text = self.find_element(*self.PRODUCT_NAME).text
        #     print(expected_text)
        self.verify_element_text(self.expected_text, *self.WISHLIST_PROD_NAME)

    def social_visible(self):
        social = self.find_element(*self.WISHLIST_SOCIAL)
        # actions = ActionChains(self.driver)
        print(social.is_displayed())
        print(social.is_enabled())

    def open_prod_page(self):
        prod_name = self.find_element(*self.WISHLIST_PROD_NAME)
        actions = ActionChains(self.driver)
        actions.move_to_element(prod_name)
        actions.click(prod_name)
        actions.perform()
        sleep(1)

    def remove_prod(self):
        remove_btn = self.find_element(*self.WISHLIST_REMOVE)
        actions = ActionChains(self.driver)
        actions.move_to_element(remove_btn)
        actions.click(remove_btn)
        actions.perform()
        sleep(1)

    def confirm_msg(self):
        expected_text = "Product successfully removed."
        # text1 = self.find_element(*self.MSG_CONFIRM)
        # print(text1.is_displayed())
        self.verify_element_text(expected_text, *self.MSG_CONFIRM)

    def select_sort_popular(self):
        sort_box = self.find_element(*self.SORT_BOX)
        select = Select(sort_box)
        select.select_by_value('popularity')

    def navigate_pages(self):
        next_pages = self.find_elements(*self.PAGINATION)
        for page in range(len(next_pages) - 1):
            next_pages = self.find_elements(*self.PAGINATION)
            next_pages[page].click()

    def select_sort_default(self):
        sort_box = self.find_element(*self.SORT_BOX)
        select = Select(sort_box)
        select.select_by_value('menu_order')
        sleep(4)

    def verify_popular_page_opened(self):
        self.verify_url_contains_query('https://gettop.us/shop/?orderby=popularity')

    def right_slider_to_left(self):
        slider = self.find_element(*self.PRICE_FILTER_SLIDER)
        filter_btn = self.find_element(*self.FILTER_BTN)
        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(slider, -300, 0)
        sleep(3)
        actions.click(filter_btn)
        actions.perform()
        sleep(5)

    def verify_no_prod_msg(self):
        expected_text = "No products were found matching your selection."
        # text1 = self.find_element(*self.FILTER_RESULT_MSG)
        # print(text1.is_displayed())
        self.verify_element_text(expected_text, *self.FILTER_RESULT_MSG)

    def right_slider_to_right(self):
        slider = self.find_element(*self.PRICE_FILTER_SLIDER2)
        filter_btn = self.find_element(*self.FILTER_BTN)
        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(slider, 300, 0)
        sleep(3)
        actions.click(filter_btn)
        actions.perform()
        sleep(3)
