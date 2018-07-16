"""抽取器，从响应结果中抽取部分数据

对接口测试来说，很多时候，我们的用例不是一次请求就OK了的，而是多个请求复合的，我们第二个请求可能会用到第一个请求返回值中的数据，这就要我们再次进行封装，做一个抽取器，从结果中抽取部分信息。
这里我们会用到JMESPath库，这是一个让我们通过类似于xpath或点分法来定位json中的节点的库


"""
import jmespath
import json
from src.utils.client import HTTPClient

class JMESPathExtractor(object):
    """
       用JMESPath实现的抽取器，对于json格式数据实现简单方式的抽取。
       """
    def extract(self,query=None,body=None):
        try:
            return jmespath.search(query,json.loads(body))
        except Exception as e:
            raise ValueError('Invalid query:'+query+':'+str(e))



if __name__ == '__main__':
    res = HTTPClient(url = 'http://wthrcdn.etouch.cn/weather_mini?citykey=101010100',method='GET').send()
    print(res.text)
    j = JMESPathExtractor()
    j_1 = j.extract(query='data.forecast[1].date',body=res.text)
    j_2 = j.extract(query='data.ganmao',body=res.text)
    print(j_1,j_2)

