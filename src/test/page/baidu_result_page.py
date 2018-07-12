from src.test.common.page import Page
from selenium.webdriver.common.by import By

class BaiDuResultPage(Page):

    loc_result_links = (By.XPATH,'//div[contains(@class, "result")]/h3/a')

    @property
    def result_links(self):
        return self.find_elements(*self.loc_result_links)
