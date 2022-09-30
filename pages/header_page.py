from pages.base_page import Page
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class Header(Page):
    CATEGORY_LINKS = (By.CSS_SELECTOR, '.flex-col.hide-for-medium.flex-left.flex-grow ul.header-nav.header-nav-main.nav.nav-left.nav-uppercase li[id*="menu-item"] a.nav-top-link')
    CATEGORY_TEXT = (By.CSS_SELECTOR, '.woocommerce-breadcrumb.breadcrumbs.uppercase')
    PRODUCTS_LINKS = (By.CSS_SELECTOR, 'div.products div.col')
    RESULTS_NUMBER = (By.CSS_SELECTOR, 'div.flex-col p.woocommerce-result-count')
    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.box-text p.name')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'div.box-text div.price-wrapper')
    PRODUCT_CATEGORY = (By.CSS_SELECTOR, 'div.box-text p.category')
    QVIEW = (By.CSS_SELECTOR, 'div.image-tools a.quick-view')
    QVIEW_X = (By.CSS_SELECTOR, 'div.mfp-wrap button.mfp-close')
    QVIEW_ADCART = (By.CSS_SELECTOR, 'form.cart button[name="add-to-cart"]')


    def category_selection(self):
        all_category = self.find_elements(*self.CATEGORY_LINKS)
        expected_text = ['HOME / LAPTOP', 'HOME / TABLET', 'HOME / SMARTPHONE', 'HOME / ACCESSORIES']
        actual_text = []

        for cat in range(len(all_category)):
            link_to_click = self.find_elements(*self.CATEGORY_LINKS)[cat]
            link_to_click.click()

            actual_text += [self.find_element(*self.CATEGORY_TEXT).text]
        assert expected_text == actual_text, \
            f'Expected text {expected_text} is not in Actual Text {actual_text}'


    def verify_count(self):
        expected_count = self.driver.find_element(*self.RESULTS_NUMBER).text
        products = self.driver.find_elements(*self.PRODUCTS_LINKS)
        actual_count = len(products)
        assert str(actual_count) in expected_count, \
            f'Expected text {actual_count} is not in Actual Text {expected_count}'

    def verify_name_cate_price(self):
        products_all = self.driver.find_elements(*self.PRODUCTS_LINKS)
        for prod in range(len(products_all)):
            self.verify_prod_category()
            self.verify_prod_name()
            self.verify_prod_price()

    def verify_prod_category(self):
        products_all = self.driver.find_elements(*self.PRODUCTS_LINKS)
        prod_category = self.driver.find_elements(*self.PRODUCT_CATEGORY)
        for cat in range(len(products_all)):
            prod_category = self.driver.find_elements(*self.PRODUCT_CATEGORY)
            # category_count = len(prod_category)
            # prod_count = len(products_all)
        assert len(products_all) == len(prod_category), \
            f"The Product count {len(products_all)} with the \ " \
            f"Category label count for products displayed {len(prod_category)}"


    def verify_prod_name(self):
        products_all = self.driver.find_elements(*self.PRODUCTS_LINKS)
        prod_name = self.driver.find_elements(*self.PRODUCT_NAME)
        for cat in range(len(products_all)):
            prod_name = self.driver.find_elements(*self.PRODUCT_NAME)
            # category_count = len(prod_category)
            # prod_count = len(products_all)
        assert len(products_all) == len(prod_name), \
            f"The Product count {len(products_all)} with the \
            Product name count for products displayed {len(prod_name)}"

    def verify_prod_price(self):
        products_all = self.driver.find_elements(*self.PRODUCTS_LINKS)
        prod_price = self.driver.find_elements(*self.PRODUCT_PRICE)
        for cat in range(len(products_all)):
            prod_category = self.driver.find_elements(*self.PRODUCT_PRICE)
            # category_count = len(prod_category)
            # prod_count = len(products_all)
        assert len(products_all) == len(prod_price), \
            f"The Product count {len(products_all)} with the \
            Price tag count for products displayed {len(prod_price)}"

    def verify_open_close_qview(self):
        prod_qview = self.find_elements(*self.QVIEW)

        for i in range(len(prod_qview)):
            if i > 2:
            # if i % 3 == 0 and i != 0:
                self.driver.execute_script("window.scrollTo(0, 600);")
                sleep(2)
            qview_prod = prod_qview[i]
            actions = ActionChains(self.driver)
            actions.move_to_element(qview_prod)
            actions.perform()
            qview_prod.click()
                # self.wait_for_element_click(qview_prod)
            sleep(2)
            self.wait_for_element_click(*self.QVIEW_X)
            # if qview_prod == prod_qview[3]:
            # # self.driver.execute_script("arguments[0].scrollIntoView();", qview_prod[3])
            #     self.find_element(*self.QVIEW).send_keys(Keys.PAGE_DOWN)

    # def verify_add_prod_qview(self):
    #     prod_view = self.find_elements(*self.QVIEW)
    #
    #     for i in range(len(prod_view)):
    #         if i > 2:
    #             self.driver.execute_script("window.scrollTo(0, 500);")
    #             sleep(2)
    #         prod_add = self.find_element(*self.QVIEW)[i]
    #         actions = ActionChains(self.driver)
    #         actions.move_to_element(prod_add)
    #         actions.perform()
    #         prod_add.click()
    #         sleep(2)
    #
    #         self.find_element(*self.QVIEW_ADCART)
    #         sleep(2)
    #         self.click(*self.QVIEW_ADCART)

    def verify_add_prod_qview(self):
        prod_qview = self.find_elements(*self.QVIEW)

        for i in range(len(prod_qview)):
            if i > 2:
                self.driver.execute_script("window.scrollTo(0, 600);")
                sleep(3)
            prod_add = self.find_elements(*self.QVIEW)[i]
            actions = ActionChains(self.driver)
            actions.move_to_element(prod_add)
            actions.perform()
            prod_add.click()
            sleep(2)

            # self.wait_for_element_click(*self.QVIEW_ADCART)
            # self.click(*self.QVIEW_ADCART)
            self.find_element(*self.QVIEW_ADCART)
            sleep(2)
            self.click(*self.QVIEW_ADCART)




