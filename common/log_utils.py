# encoding: utf-8
# @author: chen52
# @file: log_utils.py
# @time: 2021/4/24 17:39
# @desc:日志文件

import os
import logging
import time

current_path = os.path.dirname(__file__);
log_output_path =  os.path.join(current_path,'../','logs');

class LogUtils:
    def __init__(self,log_path = log_output_path):
        self.log_file_path = os.path.join(log_path,'api_tets_log_%s.log'%time.strftime('%Y%m%d'));
        self.__logger = logging.getLogger('wx_api_test_log');
        self.__logger.setLevel(logging.DEBUG);  #相当于  self.logger.setLevel(10);

        console_handler = logging.StreamHandler();
        file_handler = logging.FileHandler(self.log_file_path,'a',encoding='utf-8');
        formatter = logging.Formatter("%(asctime)s_%(name)s_%(levelname)s_%(message)s");
        console_handler.setFormatter(formatter);
        file_handler.setFormatter(formatter);

        self.__logger.addHandler(console_handler);
        self.__logger.addHandler(file_handler);

        console_handler.close();
        file_handler.close();#防止日志打印重复

    def get_logger(self):
        return self.__logger

#建议日志用一个对象去输出！！
logger = LogUtils().get_logger();

if __name__ == '__main__':
    logger.info('开始执行接口用例')


