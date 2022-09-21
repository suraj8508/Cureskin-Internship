import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app.application import Application


def browser_init(context):
    """
    :param context: Behave context
    """
    c = webdriver.ChromeOptions()
    c.add_argument("--incognito")
    context.driver = webdriver.Chrome(executable_path="./chromedriver", options=c)
    # context.browser = webdriver.Safari()
    # context.browser = webdriver.Firefox()

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    allure.attach(
        context.driver.get_screenshot_as_png(),
        name="Screenshot",
        attachment_type=AttachmentType.PNG
    )
    context.driver.delete_all_cookies()
    context.driver.quit()
