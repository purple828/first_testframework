from src.test.common.page import Page
from selenium.webdriver.common.by import By

class BaiDuMainPage(Page):

    loc_search_input = (By.ID,'kw')
    loc_search_button = (By.ID,'su')

    def search(self,kw):
        self.find_element(*self.loc_search_input).send_keys(kw)
        self.find_element(*self.loc_search_button).click()
        