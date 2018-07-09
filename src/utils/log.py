import os
import logging
from src.utils.config import Config,LOG_PATH
from logging.handlers import TimedRotatingFileHandler
'''
封装logging对象
'''
class Logger(object):

    def __init__(self,logger_name = "framework"):

        self.logger = logging.getLogger(logger_name)
        logging.root.level(logging.NOTSET)  #防止日志打印不出来
        self.log_file_name = "test.log"
        self.backup_count = 5
        #日志输出级别
        self.console_output_level = "WARINING"
        self.file_output_level = "DEBUG"
        #日志输出格式
        self.formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    def get_logger(self):
        #在logger中添加日志句柄并返回，如果logger已有句柄，则直接返回
        if not self.logger.handler : #避免重复日志
