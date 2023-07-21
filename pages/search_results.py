from selenium.webdriver.common.by import By
from pages.base_page import Page

class SearchResultsPage(Page):
    COUNT = (By.ID, "ProductCount")


    def verify_results(self):
        expected_count = 19
        actual_count = self.driver.find_element(*self.COUNT).text
        assert expected_count == actual_count, f' Expected {expected_count} search results but got {actual_count}'
