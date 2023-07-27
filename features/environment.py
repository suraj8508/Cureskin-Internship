import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app.application import Application
from selenium.webdriver.support.events import EventFiringWebDriver

bs_user = 'surajbabu_y0SqJM'
bs_key = 'uEqTUDyjrH4zaeTP3w5S'


def browser_init(context, test_name):
    """
    :param context: Behave context
    """
    ########### CHROME ##################################################
    service = Service("/Users/sbt/Documents/automation/Cureskin-Internship/chromedriver_new/chromedriver")
    # c = webdriver.ChromeOptions()
    # c.add_argument("--incognito")
    context.driver = webdriver.Chrome(service=service)
    ######################################################################

    ########## SAFARI #####################################################
    # context.driver = webdriver.Safari()
    #####################################################################

    ########## FIREFOX ####################################################
    # f_profile = webdriver.FirefoxProfile()
    # f_profile.set_preference("browser.privatebrowsing.autostart", True)
    # # context.browser = webdriver.Firefox(executable_path="/Users/sbt/Documents/automation/Cureskin-Internship/geckodriver")
    # context.driver = webdriver.Firefox(executable_path="./geckodriver", firefox_profile=f_profile)
    ######################################################################

    ##########  Headless Mode Settings ########################################
    # Headless Mode Settings
    # options = webdriver.ChromeOptions()
    # options.add_argument("--headless")
    # options.add_argument('--window-size=1920,1080')
    # context.driver = webdriver.Chrome(service=service, options=options)
    ######################################################################

    ########## MOBILE  #####################################################
    # Mobile - run tests on mobile web browser
    # service = Service("/Users/sbt/Documents/automation/Cureskin-Internship/chromedriver_new/chromedriver")
    # options = webdriver.ChromeOptions()
    # mobile_emulation = {"deviceName": "Pixel 5"}
    # options.add_experimental_option("mobileEmulation", mobile_emulation)
    # context.driver = webdriver.Chrome(chrome_options=options, service=service)
    ######################################################################

    ##########  EventFiringWebDriver - log file ###################################
    ### for drivers ###
    # context.driver = EventFiringWebDriver(webdriver.Chrome(), MyListener())
    # for headless mode ###
    # context.driver = EventFiringWebDriver(webdriver.Chrome(chrome_options = options), MyListener())
    ######################################################################

    ########## BROWSERSTACK ###############################################
    # desired_cap = {
    #     'bstack:options': {
    #         "os": "Windows",
    #         "osVersion": "11",
    #         "local": "false",
    #     },
    #     "browserName": "Chrome",
    #     "browserVersion": "114.0",
    # }
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)
    #######################################################################

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


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
