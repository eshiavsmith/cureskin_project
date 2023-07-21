from selenium.webdriver.common.by import By
from pages.base_page import Page


class ProductPage(Page):

    NAME = (By.CSS_SELECTOR, "a[href*='/products/the-good-gummy?']")
    IMAGE = (By.CSS_SELECTOR, "lazy-image.image-animate.media.media--portrait")
    PRICE = (By.CSS_SELECTOR, "div.price.price--on-sale")


    def verify_name(self):
        return self.find_elements(*self.NAME)


    def verify_image(self):
        return self.find_element(*self.IMAGE)


    def verify_price(self):
        return self.find_element(*self.PRICE)
        # prod_price = context.driver.find_elements(*self.PRICE)
        # assert len(prod_price) == 8, f"Expected price for 8 products but got {len(prod_price)}"
        # # assert expected_price == actual_price, f'Error! Expected {expected_price}'

