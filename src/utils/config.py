import os
from src.utils.file_reader import YamlReader

BASE_PATH = os.path.split(os.path.abspath(os.path.dirname(__file__)+"\.."))[0]
print(BASE_PATH) #('F:\\python\\first_testframework', 'src')    取第一个根目录
CONFIG_FILE = os.path.join(BASE_PATH,"config","config.yml")
DATA_PATH = os.path.join(BASE_PATH,"data")
DRIVER_PATH = os.path.join(BASE_PATH,"drivers")
LOG_PATH = os.path.join(BASE_PATH,"log")
REPORT_PATH = os.path.join(BASE_PATH,"report")

class Config:

    def __init__(self,config=CONFIG_FILE):
        self.config = YamlReader(config).data
        print("self.config---------------",self.config)


    def get(self,element,index=0):
        print("self.config[index].get(element)-----------",self.config[index].get(element))
        return self.config[index].get(element)



