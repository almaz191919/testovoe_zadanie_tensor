import time
from .locators import ImagePageLocators
from .base_page import BasePage

class ImagePage(BasePage):
    def check_url_imagepage(self):
        for window_handle in self.browser.window_handles:
            self.browser.switch_to.window(window_handle)
        assert 'https://yandex.ru/images/' in str(self.browser.current_url), "URL imagepage not equal 'https://yandex.ru/images/'"

    def open_first_category(self):
        try:
            self.browser.find_element(*ImagePageLocators.FIRST_CATEGORY).click()
            time.sleep(1)
        except:
            assert False, "Don't open first category"

    def open_first_pictur(self):
        try:
            self.browser.find_element(*ImagePageLocators.FIRST_PICTUR).click()
            time.sleep(0.5)
        except:
            assert False, "Don't open first picture!"

    def check_open_first_pictur(self):
        assert self.is_element_present(*ImagePageLocators.PICTUR_OPEN), "Picture is not open"
        self.src_one = str(self.browser.current_url)

    def press_next(self):
        try:
            self.browser.find_element(*ImagePageLocators.LINK_NEXT).click()
            time.sleep(0.5)
        except:
            assert False, "Don't press next picture"

    def press_back(self):
        try:
            self.browser.find_element(*ImagePageLocators.LINK_BACK).click()
            time.sleep(0.5)
        except:
            assert False, "Don't press back picture"

    def check_pictur_next(self):
        assert str(str(self.browser.current_url)) != self.src_one, "Next pictur don't open!"

    def check_open_first_pict(self):
        assert str(str(self.browser.current_url)) == self.src_one, "Open pictur not first!"