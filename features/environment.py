from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.firefox.options import Options as FirefoxOptions
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.support.wait import WebDriverWait

from app.application import Application
from support.logger import logger


def browser_init(context, test_name):
    """
    :param context: Behave context
    """
    ### SAFARI BROWSER ###
    # context.driver = webdriver.Safari()
    #############################################

    ### CHROME BROWSER ###
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)
    #############################################

    #### CHROME HEADLESS MODE ####
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    # context.driver = webdriver.Chrome(
    #     chrome_options=options,
    #     service=service
    # )
    #############################################

    ### FIREFOX BROWSER ###
    # driver_path = GeckoDriverManager().install()
    # service = FirefoxService(driver_path)
    # context.driver = webdriver.Firefox(executable_path="/Users/eshiavsmith/Desktop/cureskin_project/geckodriver")
    #############################################

    #### FIREFOX HEADLESS MODE ####
    # object of FirefoxOptions
    # options = webdriver.FirefoxOptions()
    #
    # # set options.headless to True
    # options.headless = True
    # options.add_argument('--headless')
    # context.driver = webdriver.Firefox(executable_path="/Users/eshiavsmith/Desktop/cureskin_project/geckodriver", options=options)
    #############################################

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 5)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    # print('\nStarted scenario: ', scenario.name)
    logger.info(f'Started scenario: {scenario.name}')
    browser_init(context, scenario.name)


def before_step(context, step):
    # print('\nStarted step: ', step)
    logger.info(f'Started step: {step}')


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
