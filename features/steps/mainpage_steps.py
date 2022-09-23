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


