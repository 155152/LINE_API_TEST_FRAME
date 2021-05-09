# encoding: utf-8
# @author: chen52
# @file: config_utils.py
# @time: 2021/4/24 14:32
# @desc:配置文件

#方法1
# class ConfigUtils:
#     @property #由普通方法变成属性方法
#     def HOSTS(self):
#         return 'api.weixin.qq.com'
#
# #属性方法
# config = ConfigUtils();
#
# if __name__ == '__main__':
#     #普通方法
#     #print(ConfigUtils().HOSTS())
#
#     #属性方法
#     print(config.HOSTS)

#方法2
import configparser
import os

config_file_path = os.path.join(os.path.dirname(__file__),'../','conf','config.ini');


class ConfigUtils:
    def __init__(self,config_file=config_file_path):
        self.cfg_obj = configparser.ConfigParser();
        self.cfg_obj.read(config_file_path,encoding='utf-8');

    @property
    def HOSTS(self):
        hosts_value = self.cfg_obj.get('default','HOSTS');
        return hosts_value

    @property
    def CASE_PATH(self):
        hosts_value = self.cfg_obj.get('path','case_path');
        return hosts_value

    @property
    def APPID(self):
        appid = self.cfg_obj.get('user_info','APPID');
        return appid

    @property
    def SECRET(self):
        secret = self.cfg_obj.get('user_info','SECRET');
        return secret

    @property
    def email_stmp_server(self):
        stmp_server = self.cfg_obj.get('email','STMP_SERVER')
        return stmp_server

    @property
    def email_sender(self):
        sender = self.cfg_obj.get('email','SENDER')
        return sender

    @property
    def email_receiver(self):
        receiver = self.cfg_obj.get('email','RECEIVER')
        return receiver

    @property
    def email_cc(self):
        cc = self.cfg_obj.get('email','CC')
        return cc

    @property
    def email_password(self):
        password = self.cfg_obj.get('email','PASSWORD')
        return password

config = ConfigUtils();

if __name__ == '__main__':
    print(config.HOSTS)
    print(config.CASE_PATH)

