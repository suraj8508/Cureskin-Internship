from pages.base_page import Page
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC

PRODUCT_NAME = (By.CSS_SELECTOR, 'div.box-text p.name')


@given('Open Laptop Category Page')
def open_lap_category_page(context):
    context.app.product_page.open_lap_category_page()


# @given('Open Laptop Category Page')
# def open_lap_category_page(context):
#     context.app.product_page.open_lap_category_page()


@given('Open the whole product page')
def open_whole_prod_page(context):
    context.app.product_page.open_whole_prod_page()


@given('Open the products page sorted by popularity')
def open_sort_popular_page(context):
    context.app.product_page.open_sort_popular_page()


@when('User adds the product to wishlist')
def add_prod_wishlist(context):
    context.app.product_page.add_prod_wishlist()


@when('User open the wishlist page')
def open_wishlist_page(context):
    context.app.product_page.open_wishlist_page()


@when('User selects the sort by popularity')
def select_sort_popular(context):
    context.app.product_page.select_sort_popular()


@then('User can click through sorted pages')
def navigate_pages(context):
    context.app.product_page.navigate_pages()


@then('User can reset to default sorting')
def select_sort_default(context):
    pass


@then("User verifies the correct page opened")
def verify_popular_page_opened(context):
    context.app.product_page.verify_popular_page_opened()


@then('Verify product in wishlist')
def verify_prod_in_wishlist(context):
    # expected_text = context.driver.find_element(*PRODUCT_NAME).text
    context.app.product_page.verify_prod_in_wishlist()


@then('User can open product detail page')
def open_prod_page(context):
    context.app.product_page.open_prod_page()


@then('User can see Social Logos to share')
def social_visible(context):
    context.app.product_page.social_visible()


@then('User can remove product from Wishlist')
def remove_prod(context):
    context.app.product_page.remove_prod()


@then('User Can See Confirmation Message')
def confirm_msg(context):
    context.app.product_page.confirm_msg()


