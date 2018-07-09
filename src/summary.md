## 遇到的问题
+ 1、用Pycharm工具编写代码时，webdriver导不进，本地的python编译器已经安装了selenium，原因是Pycharm软件若没有设置Project Interprester或默认选择自带的；

+ 2、若将配置信息从逻辑代码中抽取到配置文件时，需要先封装一个YamlReader对象，然后建一个读取配置文件内容的Config类； 

+ 3、logging日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET，默认的日志级别设置为WARNING，默认的日志格式为日志级别：Logger名称：用户输出消息。