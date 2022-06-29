from .locators import SearchPageLocators
from .base_page import BasePage


class SearchPage(BasePage):
    def check_frist_link_leads_to_tensor(self):
        link = self.browser.find_element(*SearchPageLocators.FIRST_SEARCH_RESULT_LINK).get_attribute("href")
        assert str(link) == "https://tensor.ru/" , "First link does not leads to tensor"

