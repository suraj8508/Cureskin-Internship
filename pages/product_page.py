from pages.base_page import Page
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class ProductPage(Page):
    expected_text = ''
    PROD_IMAGE = (By.CSS_SELECTOR, 'div.box-image img.attachment-woocommerce_thumbnail')
    WISHLIST_ICON = (By.CSS_SELECTOR, 'div.wishlist-icon i.icon-heart')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.box-text div.title-wrapper p.name a')
    WISHLIST_PROD_NAME = (By.CSS_SELECTOR, 'table.cart td.product-name a')
    WISHLIST_REMOVE =(By.CSS_SELECTOR, 'table.cart td.product-remove a')
    MSG_CONFIRM = (By.CSS_SELECTOR, 'div.woocommerce-message div.container.container')
    WISHLIST_SOCIAL =(By.CSS_SELECTOR, 'div.yith_wcwl_wishlist_footer div.social-icons a')

    def open_lap_category_page(self):
        self.open_url('product-category/laptop/')

    def open_phn_category_page(self):
        self.open_url('product-category/phone/')

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


