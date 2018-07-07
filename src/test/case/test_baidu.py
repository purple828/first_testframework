from selenium import webdriver
import time
import unittest
import os
from selenium.webdriver.common.by import By

class TestBaiDu(unittest.TestCase):
    URL = "https://www.baidu.com/";
    #获取浏览器驱动的存放的目录
    current_path = os.path.abspath(__file__)  #当前文件的绝对路径
    current_dir_path = os.path.dirname(current_path)
    base_path = current_dir_path + "\..\..\.."
    print('current_dir_path----------',current_dir_path)
    driver_path = os.path.abspath(base_path + "\drivers\chromedriver.exe")
    print('driver_path------',driver_path)
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')

    def setUp(self):
        self.driver = webdriver.Chrome(self.driver_path)
        self.driver.get(self.URL)

    def tearDown(self):
        self.driver.quit()

    def test_search_0(self):
        self.driver.find_element(By.ID,"kw").send_keys("python")
        self.driver.find_element(By.ID,"su").click()
        time.sleep(2)

        #进入python官网
        self.driver.find_element(By.XPATH,'//div[@id="1"]/h3/a[1]').click()

        #定位不到python官网的元素   ？？？
        # self.driver.find_element(By.ID,"id-search-field").send_keys("pip")
        # self.driver.find_element(By.ID,"submit").click()
        #
        # time.sleep(2)
        #
        # links = self.driver.find_element(By.XPATH,'//ul[@class="list-recent-events menu"]/li/h3/a')
        # for link in links:
        #     print('links-------',link)

    def test_search_1(self):
        self.driver.find_element(By.ID, "kw").send_keys("Python selenium")
        self.driver.find_element(By.ID, "su").click()
        time.sleep(2)
        links = self.driver.find_elements(*self.locator_result)
        for link in links:
            print(link.text)












if __name__ == "__main__":
    unittest.main()