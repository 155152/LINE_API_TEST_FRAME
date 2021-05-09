# encoding: utf-8
# @author: chen52
# @file: public_api_info.py
# @time: 2021/4/24 15:05
# @desc:所有接口公共化
import json
import jsonpath
from requests import RequestException

from common.config_utils import config
from common.log_utils import logger

def get_access_token_api(session,url_params):
    logger.info('————————————执行调用get_access_token_api接口开始——————————');
    try:
        response = session.get(url='https://%s/cgi-bin/token' % config.HOSTS,
                               params=url_params);
    except RequestException as e:
        logger.error('请求出现异常，错误原因是：%s'%e.__str__());
    finally:
        logger.info('————————————执行调用get_access_token_api接口结束——————————')
    return response

def get_access_token(session):
    url_params = {
        'grant_type': 'client_credential',
        'appid': config.APPID,
        'secret': config.SECRET
    }
    response = get_access_token_api(session,url_params);
    token_value = jsonpath.jsonpath(response.json(),'$.access_token')[0];
    return token_value

def create_user_tag_api(session, url_params, post_data):
    post_data_str = json.dumps(post_data, ensure_ascii=False);
    response = session.post(url='https://%s/cgi-bin/tags/create' % config.HOSTS,
                                 params=url_params,
                                 data=post_data_str.encode('utf-8'));
    return response

def delete_user_tag_api(session,url_params,post_data):
    response = session.post(url='https://%s/cgi-bin/tags/delete'%config.HOSTS,
                            params=url_params,
                            json=post_data)
    return response


