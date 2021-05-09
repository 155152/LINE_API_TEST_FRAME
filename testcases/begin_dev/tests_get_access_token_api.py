# encoding: utf-8
# @author: chen52
# @file: tests_get_access_token_api.py
# @time: 2021/4/24 11:53
# @desc:获取access_token接口

import unittest
import requests
import jsonpath
from common.config_utils import config
from common import public_api_info

class TestsGetAccessTokenApi(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = config.HOSTS
        self.session = requests.session();
    def tearDown(self) -> None:
        self.session.close();

    def test_01_get_access_token(self):
        #传统做法
        '''用例1：获取access_token正常通过'''
        url_params = {
           'grant_type':'client_credential',
            'appid':'wx3db2cdd240507beb',
            'secret':'a663b48fe38692c0c605bc45850abcfb'
        }

        response = self.session.get(url='https://%s/cgi-bin/token'%self.hosts,
                                   params=url_params)
        json_body = response.json();
        actual_result = jsonpath.jsonpath(json_body,'$.access_token')[0]
        self.assertTrue(actual_result)

    def test_02_grant_type_none(self):
        #高级做法
        self._testMethodName = '用例2';
        self._testMethodDoc = '验证grant_type值为空时'
        url_params = {
           'grant_type':'',
            'appid':'wx3db2cdd240507beb',
            'secret':'a663b48fe38692c0c605bc45850abcfb'
        }

        response = self.session.get(url='https://%s/cgi-bin/token'%self.hosts,
                                   params=url_params)
        json_body = response.json();
        actual_result = jsonpath.jsonpath(json_body,'$.errcode')[0]
        self.assertEqual(actual_result,40002)

    def test_03_appid_none(self):
        #调用接口公共方法
        self._testMethodName = '用例3';
        self._testMethodDoc = '验证appid为空时'
        url_params = {
           'grant_type':'client_credential',
            'appid':'',
            'secret':'a663b48fe38692c0c605bc45850abcfb'
        }

        response =public_api_info.get_access_token_api(self.session,url_params)
        json_body = response.json();
        actual_result = jsonpath.jsonpath(json_body,'$.errcode')[0]
        self.assertEqual(actual_result,41002)

if __name__ == '__mian__':
    unittest.main(verbosity=2)
