from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('open Gettop main page')
def open_main(context):
    context.app.main_page.open_main()
    # context.driver.get('https://gettop.us/')


@then('User click top banner right arrow')
def click_right_arw(context):
    context.app.main_page.click_right_arw()


@then('User click top banner left arrow')
def click_left_arw(context):
    context.app.main_page.click_left_arw()


@then('User can view Best Selling, Latest, Top Rated categories')
def footer_category_visible(context):
    context.app.main_page.footer_category_visible()


@then('User can view all products in the footer have price, name, star-rating')
def verify_prod_title_name_star(context):
    context.app.main_page.verify_prod_title_name_star()


@then('User can view "Copyright 2021" in footer')
def copyright_sign_visible(context):
    context.app.main_page.copyright_sign_visible()


@then('User can view Footer has button to go back to top')
def footer_btn_top(context):
    context.app.main_page.footer_btn_top()


@then('User can verify Footer has working links to all product categories')
def verify_prod_category_links(context):
    context.app.main_page.verify_prod_category_links()

