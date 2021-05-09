# encoding: utf-8
# @author: chen52
# @file: tests_delete_user_tag.py
# @time: 2021/4/24 18:35
# @desc:删除用户标签

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
        self._testMethodDoc = '验证不能删除用户标签0'

        token_id = public_api_info.get_access_token(self.session);

        #删除用户标签接口
        url_params = {
            'access_token':token_id
        };
        post_data_json = {"tag":{"id":0}};

        response = public_api_info.delete_user_tag_api(self.session,url_params,post_data_json);
        actual_result = jsonpath.jsonpath(response.json(),'$.errcode')[0];
        self.assertEqual(actual_result,45058)

    def test_02_create_user_tag(self):
        self._testMethodName = '用例2';
        self._testMethodDoc = '验证不能删除用户标签1'

        token_id = public_api_info.get_access_token(self.session);

        #删除用户标签接口
        url_params = {
            'access_token':token_id
        };
        post_data_json = {"tag":{"id":1}};

        response = public_api_info.delete_user_tag_api(self.session,url_params,post_data_json);
        actual_result = jsonpath.jsonpath(response.json(),'$.errcode')[0];
        self.assertEqual(actual_result,45058)

    def test_03_create_user_tag(self):
        self._testMethodName = '用例3';
        self._testMethodDoc = '验证不能删除用户标签2'

        token_id = public_api_info.get_access_token(self.session);

        #删除用户标签接口
        url_params = {
            'access_token':token_id
        };
        post_data_json = {"tag":{"id":2}};

        response = public_api_info.delete_user_tag_api(self.session,url_params,post_data_json);
        actual_result = jsonpath.jsonpath(response.json(),'$.errcode')[0];
        self.assertEqual(actual_result,45058)

if __name__ == '__main__':
    unittest.main(verbosity=2)


