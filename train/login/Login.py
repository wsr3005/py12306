# -*- coding: utf-8 -*-
# @Time    : 2019/8/13 19:30
# @Author  : wsr
# @Site    :
# @File    : Login.py
# @Software: PyCharm
import time
from collections import OrderedDict

from framework.conf.Constant import TYPE_LOGIN_N
from framework.conf.Url import loginUrls
from framework.utils import Utils
from framework.utils.log.Log import Log
from framework.utils.net.NetUtils import EasyHttp
from train.captcha.Captcha import Captcha


def login_logic(func):
    def wrapper(*args, **kwargs):
        pass
    return wrapper

class Login(object):
    def _uamtk(self):
        """

        :return: 权限token获取情况，0表示成功；message为验证通过；newapptk为uamauthclient所需要post的值
        """
        json_ret = EasyHttp.send(self._url_info['uamtk'], data={'appid': 'otn'})
        
        def is_success(response):
            return response['result_code'] == 0 if response and 'result_code' in response else False
        
        return is_success(json_ret), \
               json_ret['message'] if json_ret and 'message' in json_ret else 'no result_message', \
               json_ret['newapptk'] if json_ret and 'newapptk' in json_ret else 'no newapptk'
        
    def _uamauthclient(self, apptk):
        """

        :param apptk: _uamtk返回值
        :return: 权限获取情况，0表示成功；xxx验证通过
        """
        json_ret = EasyHttp.send(self._url_info['uamauthclient'], data={'tk': apptk})
        
        def is_success(response):
            return response['result_code'] == 0 if response and 'result_code' in response else False
        
        return is_success(json_ret), \
               '%s:%s' % (json_ret['username'],
                          json_ret['result_message']) if json_ret else 'uamauthclient failed'
    
    def _login_normal(self, username, password, type=TYPE_LOGIN_N):
        results, verify = Captcha().verify_manually(type)
        if not verify:
            return False, '验证码输入有误'
        Log.verify("验证码识别成功")
        data = OrderedDict()
        data['username'] = username
        data['password'] = password
        data['appid'] = 'otn'
        data['answer'] = results
        self._url_info = loginUrls['normal']
        response = EasyHttp.post(self._url_info['login'], data=data)
        
        def is_login_success(res_json):
            return 0 == res_json['result_code'] if res_json and 'result_code' in res_json else False, \
                   res_json['result_message'] if 'result_message' in res_json else '登陆失败'
        
        results, msg =  is_login_success(response)
        if not results:
            return False, msg
        result, msg, apptk = self._uamtk()
        if not Utils.check(results,msg):
            return False, 'uamtk failed'
        return self._uamauthclient(apptk)
        
        
if __name__ == "__main__":
    login = Login()
    login._login_normal('wyq3005', 'Mm123456')
    time.sleep(3)
    pass