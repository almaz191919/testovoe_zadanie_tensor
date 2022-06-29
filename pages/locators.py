from selenium.webdriver.common.by import By


class MainPageLocators():
    INPUT_LINK = (By.ID, "text")
    SUGGEST_LINK = (By.CLASS_NAME, 'mini-suggest__popup.mini-suggest__popup_svg_yes.mini-suggest__popup_theme_tile')
    IMAGE_LINK = (By.XPATH, '//*[@data-id="images"]')

class SearchPageLocators():
    SEARCH_RESULT = (By.ID, 'search-result')
    FIRST_SEARCH_RESULT_LINK = (By.XPATH, '//*[@id="search-result"]/li[1]//a')

class ImagePageLocators():
    FIRST_CATEGORY = (By.CLASS_NAME,'PopularRequestList-Item.PopularRequestList-Item_pos_0')
    TEXT_IN_INPUT = (By.TAG_NAME, 'title')
    FIRST_PICTUR = (By.CLASS_NAME, 'serp-item__preview')
    LINK_NEXT = (By.XPATH, '//div[contains(@class,"CircleButton_type_next")]')
    LINK_BACK = (By.XPATH, '//div[contains(@class,"CircleButton_type_prev")]')
    PICTUR_OPEN = (By.XPATH, '//img[@class="MMImage-Origin"]')
