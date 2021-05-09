# encoding: utf-8
# @author: chen52
# @file: tests_create_user_tag_api.py
# @time: 2021/4/24 13:31
# @desc:创建用户标签

import unittest
import requests
import jsonpath
import json
from common.config_utils import config
from common import public_api_info

class TestsGetAccessTokenApi(unittest.TestCase):
    def setUp(self) -> None:
        self.hosts = config.HOSTS
        self.session = requests.session();
    def tearDown(self) -> None:
        self.session.close();

    def test_01_create_user_tag(self):
        self._testMethodName = '用例1';
        self._testMethodDoc = '正常创建用户标签'

        #获取access_token
        # url_params = {
        #     'grant_type': 'client_credential',
        #     'appid': 'wx3db2cdd240507beb',
        #     'secret': 'a663b48fe38692c0c605bc45850abcfb'
        # }
        #
        # response = self.session.get(url='https://%s/cgi-bin/token' % self.hosts,
        #                             params=url_params)
        # json_body = response.json();
        # token_id = jsonpath.jsonpath(json_body, '$.access_token')[0]

        token_id = public_api_info.get_access_token(self.session);

        #创建标签接口
        url_params = {
            'access_token':token_id
        };
        post_data_json = {   "tag" : {     "name" : "sjldrklsj"   } };
        post_data_str = json.dumps(post_data_json,ensure_ascii = False);
        response = self.session.post(url='https://%s/cgi-bin/tags/create'% self.hosts,
                                     params = url_params,
                                     data=post_data_str.encode('utf-8'));
        actual_result = jsonpath.jsonpath(response.json(),'$.tag.name')[0];
        self.assertEqual(actual_result,'sjldrklsj')

    #调用接口公共方法
    def test_02_chongfu_user_tag(self):
        self._testMethodName = '用例2';
        self._testMethodDoc = '用户标签重复'

        #获取access_token
        # url_params = {
        #     'grant_type': 'client_credential',
        #     'appid': 'wx3db2cdd240507beb',
        #     'secret': 'a663b48fe38692c0c605bc45850abcfb'
        # }
        #
        # response = self.session.get(url='https://%s/cgi-bin/token' % self.hosts,
        #                             params=url_params)
        # json_body = response.json();
        # token_id = jsonpath.jsonpath(json_body, '$.access_token')[0]
        token_id = public_api_info.get_access_token(self.session);

        #创建标签接口
        url_params = {
            'access_token':token_id
        };
        post_data_json = {   "tag" : {     "name" : "sdfs"   } };
        post_data_str = json.dumps(post_data_json,ensure_ascii = False);
        response = public_api_info.create_user_tag_api(self.session,url_params,post_data_json)
        actual_result = jsonpath.jsonpath(response.json(),'$.errcode')[0];
        self.assertEqual(actual_result,45157)

if __name__ == '__mian__':
    unittest.main(verbosity=2)