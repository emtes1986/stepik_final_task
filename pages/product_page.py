import math
from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException # в начале файла


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.should_be_add_button()
        self.click_add_button()
        self.solve_quiz_and_get_code()
        self.should_be_success_message()
        self.should_be_correct_success_message()
        self.should_be_price_message()
        self.should_be_correct_price()

    def should_be_add_button(self):
        assert self.is_element_present(*ProductPageLocators.ADDTOBASKET_BTN), "Add to cart button is not presented"  

    def click_add_button(self):
        add_but = self.browser.find_element(*ProductPageLocators.ADDTOBASKET_BTN)
        add_but.click()  
    
    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), "No success message presented"

    def should_be_correct_success_message(self):
        title=self.browser.find_element(*ProductPageLocators.BOOK_TITLE)
        a=title.text
        success_message = self.browser.find_element(*ProductPageLocators.SUCCESS_MESSAGE)
        b=success_message.text
        assert a == b, f"Different title {title} and message {success_message}"

    def should_be_price_message(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_MESSAGE), "No price_message presented" 

    def should_be_correct_price(self):
        price = self.browser.find_element(*ProductPageLocators.PRICE)
        a = price.text
        price_message = self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE)
        b=price_message.text
        assert a == b, f"Different price {a} and message {b}"
