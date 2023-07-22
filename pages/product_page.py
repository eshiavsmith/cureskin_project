from selenium.webdriver.common.by import By
from pages.base_page import Page


class ProductPage(Page):
    NAME = (By.CSS_SELECTOR, "a.card-information__text.h4")
    IMAGE = (By.CSS_SELECTOR, "lazy-image.image-animate.media.media--portrait.media--hover-effect")
    PRICE = (By.CSS_SELECTOR, "div.price.price--on-sale")

    def verify_name(self):
        prod_name = len(self.find_elements(*self.NAME))
        assert prod_name == 8, f"Expected price for 8 products but got {prod_name}"

    def verify_image(self):
        prod_image = len(self.find_elements(*self.IMAGE))
        assert prod_image == 8, f"Expected 8 product images but got {prod_image}"

    def verify_price(self):
        prod_price = len(self.find_elements(*self.PRICE))
        assert prod_price == 8, f"Expected price for 8 products but got {len(prod_price)}"
        # assert expected_price == actual_price, f'Error! Expected {expected_price}'
