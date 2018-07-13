import unittest
from src.utils.config import Config,REPORT_PATH
from src.utils.client import HTTPClient
from src.utils.log import logger
from src.utils.HTMLTestRunner import HTMLTestRunner

class TestBaiDuHTTP(unittest.TestCase):

    URL = Config().get('URL')

    def setUp(self):
        self.client = HTTPClient(url = self.URL,method='GET')

    def test_baidu_http(self):
        res = self.client.send()
        logger.debug(res.text)
        self.assertIn('百度一下，你就知道',res.text)


if __name__ == 'test_baidu_http':
    report = REPORT_PATH + r'report_interface.html'
    with open(report,'wb') as f:
        runner = HTMLTestRunner(f,verbosity=2,title='接口测试报告',description='接口html报告')
        runner.run(TestBaiDuHTTP('test_baidu_http'))


