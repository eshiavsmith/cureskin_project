from selenium.webdriver.common.by import By
from pages.base_page import Page


class SearchResultsPage(Page):
    COUNT = (By.CSS_SELECTOR, "#ProductCount")

    def verify_results(self, expected_count):
        actual_count = self.driver.find_element(*self.COUNT).text
        assert expected_count == actual_count, f' Expected {expected_count} search results but got {actual_count}'
