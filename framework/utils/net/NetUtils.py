# -*- coding: utf-8 -*-
# @Time    : 2019/8/9 14:43
# @Author  : wsr
# @Site    : 
# @File    : NetUtils.py
# @Software: PyCharm
import random
import time
from http import cookiejar

import requests

from framework.conf.UserAgent import USER_AGENT


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
    
    @staticmethod
    def set_cookie(cookie_path):
        new_cookiejar = cookiejar.LWPCookieJar()
        requests.utils.cookiejar_from_dict({c.name: c.value for c in EasyHttp._session.cookies}, new_cookiejar)
        new_cookiejar.save(cookie_path, ignore_discard=True, ignore_expires=True)
    
    @staticmethod
    def load_cookie(cookie_path):
        load_cookiejar = cookiejar.LWPCookieJar()
        load_cookiejar.load(cookie_path, ignore_discard=True, ignore_expires=True)
        load_cookies = requests.utils.dict_from_cookiejar(load_cookiejar)
        EasyHttp._session.cookies =requests.utils.cookiejar_from_dict(load_cookies)
        
    @staticmethod
    def set_cookies(**kwargs):
        for k, v in kwargs.items():
            EasyHttp._session.cookies.set(k, v)
            
    @staticmethod
    def remove_cookies(key=None):
        EasyHttp._session.cookies.set(key, None) if key else EasyHttp._session.cookies.clear()
        
    @staticmethod
    def update_headers(headers):
        EasyHttp._session.headers.update(headers)
        
    @staticmethod
    def reset_headers():
        EasyHttp._session.headers.clear()
        EasyHttp._session.headers.update({
            'User-Agent': random.choice(USER_AGENT)
        })