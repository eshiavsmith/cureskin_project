from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open cureskin page')
def open_cureskin(context):
    context.app.main_page.open_main()
# print(main_pages.base_url)


@then('Verify search results count is {expected_count}')
def verify_results(context, expected_count):
    context.app.search_results.verify_results(expected_count)


@then('Verify name')
def verify_name(context):
    context.app.product_page.verify_name()
    # prod_name = context.driver.find_elements(*NAME)
    # assert len(prod_name) == 8, f"Expected price for 8 products but got {len(prod_name)}"


@then('Verify image')
def verify_image(context):
    context.app.product_page.verify_image()
    # prod_image = context.driver.find_elements(*IMAGE)
    # assert len(prod_image) == 8, f"Expected 8 product images but got {len(prod_image)}"


@then('Verify price')
def verify_price(context):
    context.app.product_page.verify_price()
    # prod_price = context.driver.find_elements(*PRICE)
    # assert len(prod_price) == 8, f"Expected price for 8 products but got {len(prod_price)}"
#     # assert expected_price == actual_price, f'Error! Expected {expected_price}'
#

sleep(1)