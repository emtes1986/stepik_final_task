from selenium import webdriver
from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    LOGIN_REGISTER_FORM = (By.CSS_SELECTOR, "#register_form") 

class ProductPageLocators():
    ADDTOBASKET_BTN = (By.CSS_SELECTOR, ".btn-add-to-basket")
    BOOK_TITLE = (By.CSS_SELECTOR, ".product_main h1")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success strong")
    PRICE_MESSAGE = (By.CSS_SELECTOR, ".alert-info strong")
    PRICE = (By.CSS_SELECTOR, "p.price_color")
