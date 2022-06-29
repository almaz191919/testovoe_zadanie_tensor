from pages.main_page import MainPage
from pages.search_page import SearchPage
from pages.image_page import ImagePage


def test_yandex_search(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    page.check_search_field()
    page.send_in_search("Тензор главная")
    page.check_suggest_field()
    page.check_enter_give_table_search_results()
    page = SearchPage(browser,link)
    page.check_frist_link_leads_to_tensor()

def test_yandex_pictur(browser):
    link = "https://yandex.ru/"
    page = MainPage(browser, link)
    page.open()
    page.check_link_image()
    page.click_link_image()
    page = ImagePage(browser, link)
    page.check_url_imagepage()
    page.open_first_category()
    page.open_first_pictur()
    page.check_open_first_pictur()
    page.press_next()
    page.check_pictur_next()
    page.press_back()
    page.check_open_first_pict()