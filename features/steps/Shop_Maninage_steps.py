from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('Open Cureskin shop Main page')
def open_main_page(context):
    context.app.shop_main_page.open_main_page()


@when('User opens the search field')
def open_search_bar(context):
    context.app.header_page.open_search_bar()


@when('User opens the search field in mobile version')
def open_search_bar_m(context):
    context.app.header_page.open_search_bar_m()


@when('Insert {search_word} in search field and click search')
def insert_search_word(context, search_word):
    context.app.header_page.insert_search_word(search_word)
    # context.app.header_page.click_search()


@then('User sees {count} products related to cure')
def verify_search_results(context, count):
    expected_text = f'{count} results found'
    context.app.search_result_page.verify_search_results(expected_text)
    pass


# @then('Verify results counts 19 products')
# def verify_results_count(context):
#     pass
