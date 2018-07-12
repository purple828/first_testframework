## 遇到的问题
+ 1、用Pycharm工具编写代码时，webdriver导不进，本地的python编译器已经安装了selenium，原因是Pycharm软件若没有设置Project Interprester或默认选择自带的；

+ 2、若将配置信息从逻辑代码中抽取到配置文件时，需要先封装一个YamlReader对象，然后建一个读取配置文件内容的Config类； 

+ 3、logging日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET，默认的日志级别设置为WARNING，默认的日志格式为日志级别：Logger名称：用户输出消息。

+ 4、获取控制台的句柄对象：console_handler = logging.StreamHandler()
     获取日志文件的句柄对象：file_handler = TimedRotatingFileHandler(filename='',when='D',interval=1,backupCount=,delay=True,encoding='utf-8')
     句柄应该设置formatter（日志输出格式）、level（日志等级），最后将句柄添加到日志对象中
     
+ 5、xlrd库中读取excel中sheet的内容时，title_line参数，用来声明是否在excel表格里有标题行，如果有标题行，返回dict列表，否则返回list列表，如下
        excel表格如下:
        
        | title1 | title2 |
        | value1 | value2 |
        | value3 | value4 |
        
        # 如果title_line=True
        [{"title1": "value1", "title2": "value2"}, {"title1": "value3", "title2": "value4"}]
        
        # 如果title_line=False
        [["title1", "title2"], ["value1", "value2"], ["value3", "value4"]]
        
+ 6、在Pycharm软件中使用Python ，HTMLTestRunner 生成测试报告时，遇到很奇怪的问题，明明运行的结果，没有任何报错，就是不生成测试报告。
      原因是编辑器为了方便用户执行测试，都有一项功能，可以用编辑器来调用unittest或者nose来执行测试用例，这种情况下，执行的只是用例或者套件，而不是整个文件，写在main里的代码是不会被执行的！！自然无法生成测试报告。
      解决方法：
      
      #原: if __name__ == '__main__':
       后：if __name__ == 'interface_demo':把main修改成自己的文件名就可以了
       
+ 7、MIME邮件Content-Type域常见的主类型：text、image、application、multipart；
     对于multipart类型，下面有三种子类型：mixed、alternative、related
     multipart/mixed可以包含附件。
     
     multipart/related可以包含内嵌资源。

     multipart/alternative 纯文本与超文本共存
     
     发送邮件时需要设置发送邮件的账号能支持smtp发送，并获取唯一的专属密码


