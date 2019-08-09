# -*- coding: utf-8 -*-
# @Time    : 2019/8/9 14:43
# @Author  : wsr
# @Site    : 
# @File    : NetUtils.py
# @Software: PyCharm
import time

import requests

def sendLogic(func):
    def wrapper(*args,**kwargs):
        for count in range(5):
            response = func(*args,**kwargs)
            if response is not None:
                return response
            else:
                time.sleep(0.1)
        return None
    
    return wrapper

class EasyHttp(object):
    _session = requests.Session()

    @staticmethod
    @sendLogic
    def send(url, params=None, data=None, **kwargs):
        try:
            response = EasyHttp._session.request(method=url['method'],
                                                 url=url['url'],
                                                 params=params,
                                                 data=data,
                                                 timeout=10,
                                                 allow_redirects=False,
                                                 **kwargs
                                                 )
            if response.status_code == requests.codes.ok:
                if 'response' in url:
                    if url['response'] == 'binary':
                        return response.content
                    if url['response'] == 'html':
                        response.encoding = response.apparent_encoding
                        return response.text
                return response.json()
        except:
            pass
        return None

    @staticmethod
    def get_session():
        return EasyHttp._session