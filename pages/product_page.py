from selenium.webdriver.common.by import By
from pages.base_page import Page


class ProductPage(Page):
    NAME = (By.CSS_SELECTOR, "a.card-information__text.h4")
    IMAGE = (By.CSS_SELECTOR, "a.card__media.media-wrapper")
    PRICE = (By.CSS_SELECTOR, "span.price-item.price-item--sale")
    RESULTS = (By.CSS_SELECTOR, "div.card-wrapper")
    RESULTS_COUNT = (By.CSS_SELECTOR, "#ProductCount")

    def verify_name(self):
        return self.find_elements(*self.NAME)
        # prod_name = len(self.find_elements(*self.NAME))
        # assert prod_name == 8, f"Expected8 products but got {prod_name}"

    def verify_image(self):
        self.find_elements(*self.IMAGE)
        # prod_image = len(self.find_elements(*self.IMAGE))
        # assert prod_image == 8, f"Expected 8 product images but got {prod_image}"

    def verify_price(self):
        return self.find_elements(*self.PRICE)
        # prod_price = len(self.find_elements(*self.PRICE))
        # assert prod_price == 8, f"Expected price for 8 products but got {len(prod_price)}"
        # assert expected_price == actual_price, f'Error! Expected {expected_price}'

    def all_prod(self):
        self.verify_element_text('19 products', *self.RESULTS)
