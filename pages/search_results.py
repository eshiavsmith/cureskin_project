from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    RESULTS_COUNT = (By.CSS_SELECTOR, "#ProductCount")

    def verify_count(self, expected_count):
        self.verify_element_text(expected_count, *self.RESULTS_COUNT)
        # assert expected_count in actual_count, f' Expected {expected_count} search results but got {actual_count}'
