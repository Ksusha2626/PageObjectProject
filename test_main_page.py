import pytest

from pages.main_page import MainPage


@pytest.mark.login
class TestLoginFromMainPage:

    def test_guest_can_go_to_login_page(self, app):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(app, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page.open()  # открываем страницу
        page.go_to_login_page()  # выполняем метод страницы - переходим на страницу логина
        page.should_be_login_link()
