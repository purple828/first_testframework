from selenium import webdriver
import time
import unittest
import os
from selenium.webdriver.common.by import By
from src.utils.config import Config , DRIVER_PATH , DATA_PATH , REPORT_PATH
from src.utils.log import logger
from src.utils.file_reader import ExcelReader
from src.utils.HTMLTestRunner import HTMLTestRunner

class TestBaiDu(unittest.TestCase):
    # URL = "https://www.baidu.com/";
    URL = Config().get("URL")
    excel = DATA_PATH + '/baidu.xlsx'
    #获取浏览器驱动的存放的目录
    # current_path = os.path.abspath(__file__)  #当前文件的绝对路径
    # current_dir_path = os.path.dirname(current_path)
    # base_path = current_dir_path + "\..\..\.."
    # print('current_dir_path----------',current_dir_path)
    # driver_path = os.path.abspath(base_path + "\drivers\chromedriver.exe")
    driver_path = os.path.abspath(DRIVER_PATH + "\chromedriver.exe")
    # print('driver_path------',driver_path)

    locator_kw = (By.ID, 'kw')
    locator_su = (By.ID, 'su')
    locator_result = (By.XPATH, '//div[contains(@class, "result")]/h3/a')


    # def setUp(self):
    #     self.driver = webdriver.Chrome(self.driver_path)
    #     self.driver.get(self.URL)
    #
    # def tearDown(self):
    #     self.driver.quit()

    def sub_setUp(self):
        self.driver = webdriver.Chrome(executable_path=DRIVER_PATH + '\chromedriver.exe')
        self.driver.get(self.URL)

    def sub_tearDown(self):
        self.driver.quit()

    # def test_search_0(self):
    #     self.driver.find_element(By.ID,"kw").send_keys("python")
    #     self.driver.find_element(By.ID,"su").click()
    #     time.sleep(2)
    #
    #     #进入python官网
    #     self.driver.find_element(By.XPATH,'//div[@id="1"]/h3/a[1]').click()

        #定位不到python官网的元素   ？？？
        # self.driver.find_element(By.ID,"id-search-field").send_keys("pip")
        # self.driver.find_element(By.ID,"submit").click()
        #
        # time.sleep(2)
        #
        # links = self.driver.find_element(By.XPATH,'//ul[@class="list-recent-events menu"]/li/h3/a')
        # for link in links:
        #     print('links-------',link)

    # def test_search_1(self):
    #     self.driver.find_element(By.ID, "kw").send_keys("Python selenium")
    #     self.driver.find_element(By.ID, "su").click()
    #     time.sleep(2)
    #     links = self.driver.find_elements(*self.locator_result)
    #     for link in links:
    #         # print(link.text)
    #         logger.info(link.text)

    #   参数化
    def test_search(self):
        datas = ExcelReader(self.excel).data
        logger.info(datas)
        for d in datas:
            with self.subTest(data = d):
                self.sub_setUp()
                self.driver.find_element(*self.locator_kw).send_keys(d['search'])
                self.driver.find_element(*self.locator_su).click()
                time.sleep(2)
                links = self.driver.find_elements(*self.locator_result)
                for link in links:
                    logger.info(link.text)
                self.sub_tearDown()


# if __name__ == "__main__":
if __name__ == 'test_baidu':
    report = REPORT_PATH + r'\report.html'
    print('report----------',report)
    with open(report,'wb') as f:
        runner = HTMLTestRunner(f,verbosity=2,title='从0搭建测试框架 灰蓝',description='修改html报告')
        runner.run(TestBaiDu('test_search'))
    # unittest.main()



