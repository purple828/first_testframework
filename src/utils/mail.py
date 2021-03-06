from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import re
from src.utils.log import logger
import smtplib
from socket import gaierror, error



class Email:

    def __init__(self,server,sender,password,receiver,title,message=None,path=None):
        """初始化Email

               :param title: 邮件标题，必填。
               :param message: 邮件正文，非必填。
               :param path: 附件路径，可传入list（多附件）或str（单个附件），非必填。
               :param server: smtp服务器，必填。
               :param sender: 发件人，必填。
               :param password: 发件人密码，必填。
               :param receiver: 收件人，多收件人用“；”隔开，必填。
               """
        self.title = title
        self.message = message
        self.server = server
        self.sender = sender
        self.password = password
        self.receiver = receiver
        self.files = path

        self.msg = MIMEMultipart('related')


    #将单个文件添加到附件列表
    def _attach_file(self,att_file):
        print('def -attach_file 入参：att_file = {}',att_file)
        att = MIMEText(open('%s'%att_file,'rb').read(),'plain','utf-8')
        att["Content-Type"] = 'application/octet-stream'
        file_name = re.split(r'[\\|/]',att_file)
        print('----------------------file_name = ', file_name)
        att["Content-Disposition"] = 'attachment;file_name = %s'%file_name[-1]
        self.msg.attach(att)
        logger.info('attach file {}'.format(att_file))


    def send(self):
        self.msg['Subject'] = self.title
        self.msg['From'] = self.sender
        self.msg['To'] = self.receiver
        #正文
        if self.message:
            self.msg.attach(MIMEText(self.message))

        #附件
        if self.files:
            if isinstance(self.files,list):
                for f in self.files:
                    self._attach_file(f)
            elif isinstance(self.files,str):
                self._attach_file(self.files)


        #连接服务器并发送
        try:
            smtp_server = smtplib.SMTP(self.server)
        except (gaierror and error) as e:
            logger.exception('发送邮件失败,无法连接到SMTP服务器，检查网络以及SMTP服务器. %s', e)
        else:
            try:
                smtp_server.login(self.sender,self.password)
            except smtplib.SMTPAuthenticationError as e:
                logger.exception('用户名密码验证失败！%s', e)
            else:
                smtp_server.sendmail(self.sender,self.receiver.split(';'),self.msg.as_string())
            finally:
                smtp_server.quit()
                logger.info('发送邮件"{0}"成功! 收件人：{1}。如果没有收到邮件，请检查垃圾箱，'
                            '同时检查收件人地址是否正确'.format(self.title, self.receiver))


