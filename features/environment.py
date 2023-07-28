import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.support.wait import WebDriverWait

from app.application import Application
from support.logger import logger


# Allure command:
#python3 -m behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/cureskin_test1.feature

def browser_init(context, test_name):
    """
    :param context: Behave context
    :param test_name: scenario.name
    """
    ### SAFARI BROWSER ###
    # context.driver = webdriver.Safari()
    #############################################

    ### CHROME BROWSER ###
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)
    #############################################

    ### FIREFOX BROWSER ###
    # driver_path = GeckoDriverManager().install()
    # service = FirefoxService(driver_path)
    # context.driver = webdriver.Firefox(executable_path="/Users/eshiavsmith/Desktop/cureskin_project/geckodriver")
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

    #### FIREFOX HEADLESS MODE ####
    # # object of FirefoxOptions
    # options = webdriver.FirefoxOptions()
    #
    # # set options.headless to True
    # options.headless = True
    # options.add_argument('--headless')
    # context.driver = webdriver.Firefox(executable_path="/Users/eshiavsmith/Desktop/cureskin_project/geckodriver", options=options)
    #############################################

    #### BROWSERSTACK ####
    # context.driver.execute_script(
    #     'browserstack_executor:{"action": "setSessionName", "arguments": {"name": " ' + scenario.name + ' " }}')

    # desired_cap = {
    #     'os': 'Windows',
    #     'osVersion': '11',
    #     'browserVersion': 'latest',
    #     'browserName': 'Firefox',
    #     'name': test_name
    # }
    options = FirefoxOptions()
    caps = {
        "os": "OS X",
        "osVersion": "Catalina",
        "buildName": "firefoxprofile- node",
        "sessionName": test_name,
        "local": "false",
    }
    options.set_capability('bstack:options', caps)
    options.set_capability('browserVersion', '95')
    options.set_capability('browserName', 'Firefox')
    bs_user = 'eshiasmith_bqH79Y'
    bs_key = 'xSUuBdnUumwSqUULtcsg'
    url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    context.driver = webdriver.Remote(url, options=options)

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
        logger.error(f'Step failed: {step}')
        print('\nStep failed: ', step)
        # Mark test case as FAILED on BrowserStack:
        # Documentation: https://www.browserstack.com/docs/automate/selenium/view-test-results/mark-tests-as-pass-fail
        context.driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": '
            '{"status":"failed", "reason": "Step failed"}}'
        )

        # Attach a screenshot to Allure report in case the step fails:
        # allure.attach(
        #     context.driver.get_screenshot_as_png(),
        #     name=f'{step.name}.png',
        #     attachment_type=AttachmentType.PNG
        # )


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
