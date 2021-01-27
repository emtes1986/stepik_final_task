from .base_page import BasePage
from .locators import BasketPageLocators
from selenium.common.exceptions import NoAlertPresentException

class BasketPage(BasePage):

    def basket_should_be_empty(self):
    	assert self.is_not_element_present(*BasketPageLocators.PRODUCT_TITLE), \
       "There is something in basket, but should not be"
    
    def should_be_empty_message(self):
        expected_alert = 'basket is empty'
        alert = self.browser.find_element(*BasketPageLocators.EMPTY_MESSAGE).text
        assert expected_alert in alert, "Text 'Basket is empty' should be present"
