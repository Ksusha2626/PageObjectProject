import faker
import pytest

from pages.product_page import ProductPage
from pages.login_page import LoginPage
from pages.basket_page import BasketPage

COMMON_PRODUCT_LINK = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
LOGIN_LINK = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'

urls = [f"{COMMON_PRODUCT_LINK}/?promo=offer{no}" for no in range(6)]


@pytest.mark.product_page
class TestFromProductPage:

    @pytest.mark.need_review
    @pytest.mark.parametrize('link', urls)
    def test_guest_can_add_product_to_basket(self, app, link):
        page = ProductPage(app, link)
        page.open()
        page.add_to_basket()
        page.solve_quiz_and_get_code()
        page.check_product_was_added()
        product_price = page.price_of_product()
        page.check_total_price(product_price)

    @pytest.mark.xfail(reason="Success message is present after_adding_product_to_basket")
    def test_guest_cant_see_success_message_after_adding_product_to_basket(self, app):
        page = ProductPage(app, COMMON_PRODUCT_LINK)
        page.open()
        page.add_to_basket()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(self, app):
        page = ProductPage(app, COMMON_PRODUCT_LINK)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.xfail(reason="Success message is not disappeared_after_adding_product_to_basket")
    def test_message_disappeared_after_adding_product_to_basket(self, app):
        page = ProductPage(app, COMMON_PRODUCT_LINK)
        page.open()
        page.add_to_basket()
        page.element_should_disappear()

    def test_guest_should_see_login_link_on_product_page(self, app):
        page = ProductPage(app, COMMON_PRODUCT_LINK)
        page.open()
        page.should_be_login_link()

    @pytest.mark.need_review
    def test_guest_can_go_to_login_page_from_product_page(self, app):
        page = ProductPage(app, COMMON_PRODUCT_LINK)
        page.open()
        page.go_to_login_page()

    @pytest.mark.need_review
    def test_guest_cant_see_product_in_basket_opened_from_product_page(self, app):
        page = ProductPage(app, COMMON_PRODUCT_LINK)
        page.open()
        page.go_to_basket()
        page = BasketPage(app, COMMON_PRODUCT_LINK)
        page.check_empty_basket()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(autouse=True)
    def setup(self, app):
        login_page = LoginPage(app, LOGIN_LINK)
        login_page.open()
        f = faker.Faker()
        email = f.email()
        password = f.password()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, app):
        page = ProductPage(app, COMMON_PRODUCT_LINK)
        page.open()
        page.add_to_basket()
        page.check_product_was_added()
        product_price = page.price_of_product()
        page.check_total_price(product_price)

    def test_user_cant_see_success_message(self, app):
        page = ProductPage(app, COMMON_PRODUCT_LINK)
        page.open()
        page.should_not_be_success_message()
