# encoding: utf-8
# @author: chen52
# @file: email_utils.py
# @time: 2021/4/25 13:45
# @desc:邮箱配置

import smtplib
import email
import os

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from common.config_utils import config

class EmailUtils:
    def __init__(self,email_body,email_attach_path = None):
        self.stmp_server = config.email_stmp_server
        self.sender= config.email_sender
        self.receiver = config.email_receiver
        self.cc = config.email_cc
        self.password = config.email_password
        self.subject = '自动化测试报告';
        self.body = email_body;
        self.attath_path = email_attach_path

    def email_body(self):
        email_obj = MIMEMultipart();
        email_obj['from'] = self.sender;  # 发件人
        email_obj['to'] = self.receiver; # 收件人
        email_obj['Cc'] = self.cc; # 抄送人
        email_obj['subject'] = self.subject;
        email_obj.attach(MIMEText(self.body,'html','utf-8'));

        if self.attath_path:
            # 做附件
            attach_file = MIMEText(open(self.attath_path, 'rb').read(), 'base64', 'utf-8');
            attach_file['Content-type'] = 'application/octet-stream';
            attach_file.add_header('Content-Disposition', 'attachment', filename=('gbk', '', os.path.basename(self.attath_path)));
            email_obj.attach(attach_file)
        return email_obj

    def send_email(self):
        smtp = smtplib.SMTP();
        smtp.connect(self.stmp_server);
        smtp.login(user=self.sender,password=self.password);
        smtp.sendmail(self.sender,self.receiver.split(",")+self.cc.split(","),self.email_body().as_string());
        smtp.close()

if __name__ == '__main__':
    email_body = '''
    <h1 align = "center">接口自动化测试报告</h1>
    <p align = "center">详情见附件ffffffff</h1>
    '''
    html_file_path = os.path.join(os.path.dirname(__file__), '../', 'html_reports', 'WX_API_TEST_V1.0',
                                  'WX_API_TEST_V1.0.html')
    EmailUtils(email_body,html_file_path).send_email()
