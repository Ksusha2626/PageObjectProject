from selenium.webdriver.common.by import By


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    REGISTRATION_EMAIL = (By.NAME, 'registration-email')
    REGISTRATION_PASSWORD = (By.NAME, 'registration-password1')
    REGISTRATION_PASSWORD_REPEAT = (By.NAME, 'registration-password2')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
    REGISTRATION_SUBMIT = (By.NAME, 'registration_submit')


class AddProductPageLocators:
    BASKET_BUTTON = (By.CSS_SELECTOR, '.btn-group a.btn.btn-default')
    ADD_TO_BASKET = (By.CSS_SELECTOR, '.btn-add-to-basket')
    CHECK_PRODUCT_WAS_ADDED = (By.XPATH, "//div[@id='messages']/div/div/strong[1]")

    PRODUCT_NAME = (By.CSS_SELECTOR, 'div.product_main h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, '.product_main .price_color')
    TOTAL_PRICE = (By.CSS_SELECTOR, '.alert-info .alertinner strong')


class BasketPageLocators:
    EMPTY_CART_MESSAGE = (By.ID, 'content_inner')
