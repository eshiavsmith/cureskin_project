from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

NAME = (By.CSS_SELECTOR, "a.card-information__text.h4")
IMAGE = (By.CSS_SELECTOR, "a.card__media.media-wrapper")
PRICE = (By.CSS_SELECTOR, "span.price-item.price-item--sale")
RESULTS_COUNT = (By.CSS_SELECTOR, "#ProductCount")
RESULTS = (By.CSS_SELECTOR, "div.card-wrapper")


@given('Open cureskin page')
def open_cureskin(context):
    context.app.main_page.open_main()


# print(main_pages.base_url)


@then('Verify search results count is {expected_count}')
def verify_count(context, expected_count):
    actual_count = context.driver.find_element(*RESULTS_COUNT).text
    assert expected_count == actual_count, f'Error! Expected {expected_count}, but got {actual_count}'
    # context.app.search_results_page.verify_count(actual_count)


@then('Verify first results have name')
def verify_name(context):
    context.app.product_page.verify_name()


@then('Verify first results have image')
def verify_image(context):
    context.app.product_page.verify_image()
    all_products = context.driver.find_elements(*RESULTS)
    # print(all_products)

    @then('Verify first results have price')
    def verify_price(context):
        context.app.product_page.verify_price()
        # prod_price = context.driver.find_elements(*PRICE)
        # print(prod_price)

    for product in all_products:
        name = product.find_element(*NAME).text
        price = product.find_element(*PRICE).text
        assert name, 'Name should not be blank'
        assert price, 'Price should not be blank'
        assert product.find_element(*IMAGE).is_displayed(), 'Image not Found'


sleep(1)
