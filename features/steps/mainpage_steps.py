from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@given('open Gettop main page')
def open_main(context):
    context.app.main_page.open_main()
    # context.driver.get('https://gettop.us/')
