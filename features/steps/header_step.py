from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@when('User select category and verify correct category displayed')
def category_selection(context):
    context.app.header_page.category_selection()


# @then('Items of the Correct Category displayed')
# def verify_correct_category(context):
#     # expected_text = context.driver.find_element(*)
#     context.app.header_page.verify_correct_category()


@then('Verify showing all N results reflects correct count of items')
def verify_count(context):
    context.app.header_page.verify_count()


@then('Verify all items have Category, Name and Price')
def verify_name_cate_price(context):
    context.app.header_page.verify_name_cate_price()


@then('Verify user can open and Close the Quick View')
def verify_open_close_qview(context):
    context.app.header_page.verify_open_close_qview()


@then('Verify user can add product to cart from Quick View')
def verify_add_prod_qview(context):
    context.app.header_page.verify_add_prod_qview()
