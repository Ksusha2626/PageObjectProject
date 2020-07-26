from pages.base_page import BasePage
from .locators import AddProductPageLocators


class ProductPage(BasePage):

    def add_to_basket(self):
        button = self.app.find_element(*AddProductPageLocators.ADD_TO_BASKET)
        button.click()

    def name_of_product(self):
        product_name = self.app.find_element(*AddProductPageLocators.PRODUCT_NAME).text
        return product_name

    def price_of_product(self):
        product_price = self.app.find_element(*AddProductPageLocators.PRODUCT_PRICE).text
        return product_price

    def check_product_was_added(self):
        alert = self.app.find_element(*AddProductPageLocators.CHECK_PRODUCT_WAS_ADDED).text
        product_name = self.name_of_product()
        assert alert == product_name

    def check_total_price(self, price_to_check):
        basket_price = self.app.find_element(*AddProductPageLocators.TOTAL_PRICE).text
        assert basket_price == price_to_check

    def should_not_be_success_message(self):
        assert not self.is_element_present(*AddProductPageLocators.CHECK_PRODUCT_WAS_ADDED), \
            "Element is presented, but should not be"

    def element_should_disappear(self):
        assert self.is_disappeared(*AddProductPageLocators.CHECK_PRODUCT_WAS_ADDED), \
            "Element is not disappear, but should not be"

    def go_to_basket(self):
        basket_link = self.app.find_element(*AddProductPageLocators.BASKET_BUTTON)
        basket_link.click()
