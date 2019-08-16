# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 15:23
# @Author  : wsr
# @Site    : 
# @File    : Captcha.py
# @Software: PyCharm
import time
from io import BytesIO

from PIL import Image

from framework.conf.Constant import TYPE_LOGIN_N, TYPE_LOGIN_O
from framework.conf.Url import loginUrls
from framework.utils.log.Log import Log
from framework.utils.net.NetUtils import EasyHttp


class Captcha(object):
    def get_img(self, type=TYPE_LOGIN_N):
        """

        :param type: 登录接口类型
        :return: 验证码图片（二进制形式）
        """
        url = loginUrls['other']['captcha'] if type == TYPE_LOGIN_O else loginUrls['normal']['captcha']
        Log.verify('正在获取验证码..')
        return EasyHttp.send(url)
    
    def index2coor(self, index):
        """

        :param index: 输入的验证码位置
        :return: 验证码实际坐标
        """
        solution = ['35,32', '107,38', '174,31', '246,33', '39,102', '104,106', '172,108', '247,103']
        index_list = index.split(',')
        coor_list = []
        for i in index_list:
            coor_list.append(solution[int(i)])
        coor_ans = ','.join(coor_list)
        return coor_ans
    
    def captcha_check(self, coor):
        """

        :param coor: 验证码坐标（答案）
        """
        data = {
            'answer': coor,
            'login_site': 'E',
            'rand': 'sjrand',
            '_': int(time.time() * 1000)
        }
        json_ret = EasyHttp.send(loginUrls['normal']['captchaCheck'], params=data)
        def verify(response):
            return response['result_code'] == '4' if 'result_code' in response else False
        return verify(json_ret)
    
    def verify_manually(self, type=TYPE_LOGIN_N):
        """

        :param type: 登录接口类型
        :return: 验证码坐标，验证结果
        """
        img = None
        try:
            img = Image.open(BytesIO(self.get_img(type)))
            img.show()
            Log.verify(
                """
                -----------------
                | 0 | 1 | 2 | 3 |
                -----------------
                | 4 | 5 | 6 | 7 |
                ----------------- """
            )
            results = input("请输入验证码位置，以','分割:")
        except BaseException as e:
            return None, False
        finally:
            if img is not None:
                img.close()
        coor = self.index2coor(results)
        Log.verify('验证码坐标：%s' % coor)
        return results, self.captcha_check(coor)