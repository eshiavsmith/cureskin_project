from pages.header_page import HeaderPage
from pages.main_page import MainPage
from pages.search_results import SearchResultsPage
from pages.signin_page import SignInPage
from pages.cart_page import CartPage
from pages.product_page import ProductPage
class Application:
    def __init__(self, driver):
        self.driver = driver
        #must provide selenium driver


        self.header_page = HeaderPage(self.driver)
        self.main_page = MainPage(self.driver)
        self.search_results = SearchResultsPage(self.driver)
        self.signin_page = SignInPage(self.driver)
        self.cart_page = CartPage(self.driver)
        self.product_page = ProductPage(self.driver)