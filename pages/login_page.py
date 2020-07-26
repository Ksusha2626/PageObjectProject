from pages.base_page import BasePage
from .locators import BasePageLocators


class LoginPage(BasePage):

    def register_new_user(self, email, password):
        reg_email = self.app.find_element(*BasePageLocators.REGISTRATION_EMAIL)
        reg_email.send_keys(email)
        reg_password = self.app.find_element(*BasePageLocators.REGISTRATION_PASSWORD)
        reg_password.send_keys(password)
        reg_password_repeat = self.app.find_element(*BasePageLocators.REGISTRATION_PASSWORD_REPEAT)
        reg_password_repeat.send_keys(password)
        submit = self.app.find_element(*BasePageLocators.REGISTRATION_SUBMIT)
        submit.click()
