import time
from selenium.webdriver.common.keys import Keys
from .base_page import BasePage
from .locators import MainPageLocators, SearchPageLocators
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MainPage(BasePage):

    def check_search_field(self):
        assert self.is_element_present(*MainPageLocators.INPUT_LINK), "Search field is not find"

    def send_in_search(self, request):
        try:
            search = self.browser.find_element(*MainPageLocators.INPUT_LINK)
            search.send_keys(request)
        except:
            assert False, "Don't send in search"

    def check_suggest_field(self):
        timeout = 5
        assert WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(MainPageLocators.SUGGEST_LINK)), "Suggest is not find"

    def check_enter_give_table_search_results(self):
        self.browser.find_element(*MainPageLocators.INPUT_LINK).send_keys(Keys.ENTER)
        assert self.is_element_present(*SearchPageLocators.SEARCH_RESULT), "When press Enter, the search results table does not appear"

    def check_link_image(self):
        timeout = 3
        assert WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located(MainPageLocators.IMAGE_LINK)), "Image link not find"


    def click_link_image(self):
        try:
            self.browser.find_element(*MainPageLocators.IMAGE_LINK).click()
            time.sleep(1)
        except:
            assert False, "Don't click link image"