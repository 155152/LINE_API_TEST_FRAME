# encoding: utf-8
# @author: chen52
# @file: run_all_cases.py
# @time: 2021/4/24 11:52
# @desc:

import unittest
import os
import sys
import shutil
from common import HTMLTestReportCN
from common.log_utils import logger
from common.email_utils import EmailUtils

current_path = os.path.dirname(__file__);
case_path = os.path.join(current_path,'testcases');

html_report_path = os.path.join(current_path,'html_reports/');

logger.info('—————接口测试用例开始执行—————')

discover_cases = unittest.defaultTestLoader.discover(
    start_dir=case_path,
    pattern='tests*.py'
);
api_case_suite = unittest.TestSuite();
api_case_suite.addTest(discover_cases);

#创建测试报告路径对象
html_report_path_obj = HTMLTestReportCN.ReportDirectory(html_report_path);
html_report_path_obj.create_dir('WX_API_TEST_');#创建测试报告路径
#获取测试报告网页文件的路径
html_report_file_path = HTMLTestReportCN.GlobalMsg.get_value('report_path');
html_report_file_obj = open(html_report_file_path,'wb');

runner = HTMLTestReportCN.HTMLTestRunner(stream=html_report_file_obj,
                                         tester='xiyyaw',
                                         title='微信公众平台接口测试项目',
                                         description='实战应用')

# unittest.main(verbosity=2,defaultTest='api_case_suite')
runner.run(api_case_suite)

#发邮件
email_body = '''
<h1 align = "center">接口自动化测试报告</h1>
<p align = "center">详情见附件ffffffff</p>
'''
# EmailUtils(email_body,html_report_file_path).send_email()

shutil.copyfile(html_report_file_path,'%s/WX_API_TEST.html'%sys.argv[1])






