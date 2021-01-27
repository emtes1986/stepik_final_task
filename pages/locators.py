from selenium import webdriver
from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTER_FORM = (By.CSS_SELECTOR, "#register_form") 

class ProductPageLocators():
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main>h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    ALERT_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div.alertinner")

class BasketPageLocators():
    EMPTY_MESSAGE = (By.CSS_SELECTOR, "div#content_inner p")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".basket-items .row")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, "//a[contains(text(), 'View basket')]")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
