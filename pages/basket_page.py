from pages.base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):

    def check_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_CART_MESSAGE), "No message about empty basket"
