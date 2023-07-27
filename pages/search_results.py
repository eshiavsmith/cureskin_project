from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    COUNT = (By.CSS_SELECTOR, "div.product-count")

    def verify_count(self, expected_count):
        self.verify_element_text(expected_count, *self.COUNT)
        # assert expected_count in actual_count, f' Expected {expected_count} search results but got {actual_count}'
