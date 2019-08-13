import random
import time
loginUrls = {
    'normal': {
        'index':{
            'url': r'https://www.12306.cn/index/',
            'method': 'GET',
            'headers': {
                'Accept': r'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Upgrade-Insecure-Requests': '1',
            },
            'response': 'html',
        },
        'conf':{
            'url':'https://kyfw.12306.cn/otn/login/conf',
            'method': 'POST',
            'response': 'html',
        },
        'init': {
            'url': r'https://kyfw.12306.cn/otn/login/init',
            'method': 'GET',
            'headers': {
                'Accept': r'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Referer': r'https://kyfw.12306.cn/otn/leftTicket/init',
            },
            'response': 'html',
        },
        'loginInit': {
            'url': r'https://kyfw.12306.cn/otn/resources/login.html',
            'method': 'GET',
            'headers': {
                'Accept': r'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Referer': r'https://www.12306.cn/index/',
                'Upgrade-Insecure-Requests': '1',
                'Accept-Encoding':'gzip, deflate, br',
            },
            'response': 'html',
        },
        'uamtk': {
            'url': r'https://kyfw.12306.cn/passport/web/auth/uamtk',
            'method': 'POST',
            'headers': {
                r'Content-Type': r'application/x-www-form-urlencoded; charset=UTF-8',
                'Referer': r'https://kyfw.12306.cn/otn/resources/login.html',
            }
        },
        'uamtk-static':{
            'url': r'https://kyfw.12306.cn/passport/web/auth/uamtk-static',
            'method': 'POST',
            'headers': {
                r'Content-Type': r'application/x-www-form-urlencoded; charset=UTF-8',
                'Referer': r'https://kyfw.12306.cn/otn/resources/login.html',
            }
        },
        'captcha': {
            'url': r'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand&{}'
                .format(random.random()),
            'method': 'GET',
            'response': 'binary',
            'Referer': r'https://kyfw.12306.cn/otn/resources/login.html',
        },
        "loginCaptchaCode": {  # 登录验证码
                "req_url": "/passport/captcha/captcha-image64?login_site=E&module=login&rand=sjrand&{0}&callback=jQuery19108016482864806321_1554298927290&_=1554298927293".format(random.random()),
                "req_type": "get",
                "Referer": "https://kyfw.12306.cn/otn/resources/login.html",
                "Host": "kyfw.12306.cn",
            },
        'captchaCheck': {
            'url': r'https://kyfw.12306.cn/passport/captcha/captcha-check',
            'method': 'GET',
            'headers': {
                'Content-Type': r'application/x-www-form-urlencoded; charset=UTF-8',
                'Referer': r'https://kyfw.12306.cn/otn/resources/login.html',
            }
        },
        'login': {
            'url': r'https://kyfw.12306.cn/passport/web/login',
            'method': 'POST',
            'headers': {
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Referer': 'https://kyfw.12306.cn/otn/resources/login.html',
                'Accept' : 'application/json, text/javascript, */*; q=0.01',
                'Origin':'https://kyfw.12306.cn',
                'Host':'kyfw.12306.cn',
                'Accept-Encoding':'gzip, deflate, br',
                'Accept-Language':'zh-CN,zh;q=0.9'
            }
        },
        'userLogin': {
            'url': r'https://kyfw.12306.cn/otn/login/userLogin',
            'method': 'GET',
            'headers': {
                'Content-Type': 'application/x-www-form-urlencoded',
                'Referer': 'https://kyfw.12306.cn/otn/resources/login.html',
                'Upgrade-Insecure-Requests':'1',
                'Accept-Encoding':'gzip, deflate, br',
                'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            },
            'response': 'html',
        },
        'userLoginRedirect': {
            'url': r'https://kyfw.12306.cn/otn/passport?redirect=/otn/login/userLogin',
            'method': 'GET',
            'response': 'html',
            'Upgrade-Insecure-Requests':'1',
            'Referer': 'https://kyfw.12306.cn/otn/resources/login.html'
        },
        'uamauthclient': {
            'url': r'https://kyfw.12306.cn/otn/uamauthclient',
            'method': 'POST',
            'headers': {
                'Referer': r'https://kyfw.12306.cn/otn/passport?redirect=/otn/login/userLogin',
            }
        },
        'checkUser': {
            'url': r'https://kyfw.12306.cn/otn/login/checkUser',
            'method': 'POST',
            'headers': {
                'Referer': r'https://kyfw.12306.cn/otn/leftTicket/init',
                'Content-Type': r'application/x-www-form-urlencoded; charset=UTF-8',
            }
        },
        'loginOut': {
            'url': r'https://kyfw.12306.cn/otn/login/loginOut',
            'method': 'GET',
            'headers': {
                'Referer': r'https://kyfw.12306.cn/otn/index/initMy12306',
            },
            'response': 'html',
        },
        "getDevicesId": {  # 获取用户信息
            "url": "https://kyfw.12306.cn/otn/HttpZF/logdevice?algID=7uavUD4Jd4&hashCode=HOZOxxdIBd2qLGoJqA0iStx-P1n86WFZ6Gds9U4-XyU&FMQw=1&q4f3=zh-CN&VPIf=1&custID=133&VEek=unknown&dzuS=0&yD16=0&EOQP=382b3eb7cfc5d30f1b59cb283d1acaf3&lEnu=3232235885&jp76=52d67b2a5aa5e031084733d5006cc664&hAqN=Linux%20x86_64&platform=WEB&ks0Q=d22ca0b81584fbea62237b14bd04c866&TeRS=1003x1920&tOHY=24xx1080x1920&Fvje=i1l1o1s1&q5aJ=-8&wNLf=99115dfb07133750ba677d055874de87&0aew=Mozilla/5.0%20(X11;%20Linux%20x86_64)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/75.0.3770.142%20Safari/537.36&E3gR=7484b4d443309cac29a8c080495fc1c0&timestamp=",
            "method": "GET",
            'headers' :{
            'Host': 'kyfw.12306.cn',
            'Referer': 'https://kyfw.12306.cn/otn/resources/login.html',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
        }
        }
    },
    # --------------------------------------------------------------------------------------------------------
    'other': {
        'init': {
            'url': r'https://kyfw.12306.cn/otn/login/init',
            'method': 'GET',
            'headers': {
                'Accept': r'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                r'Content-Type': r'application/x-www-form-urlencoded',
                'Referer': r'https://kyfw.12306.cn/otn/leftTicket/init',
            },
            'response': 'html',
        },'loginInit': {
            'url': r'https://kyfw.12306.cn/otn/resources/login.html',
            'method': 'GET',
            'headers': {
                'Accept': r'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                'Referer': r'https://www.12306.cn/index/',
            },
            'response': 'html',
        },
        'uamtk': {
            'url': r'https://kyfw.12306.cn/passport/web/auth/uamtk',
            'method': 'POST',
            'headers': {
                r'Content-Type': r'application/x-www-form-urlencoded; charset=UTF-8',
                'Referer': r'https://kyfw.12306.cn/otn/passport?redirect=/otn/login/userLogin',
            }
        },'uamtk-static':{
            'url': r'https://kyfw.12306.cn/passport/web/auth/uamtk-static',
            'method': 'POST',
            'headers': {
                r'Content-Type': r'application/x-www-form-urlencoded; charset=UTF-8',
                'Referer': r'https://kyfw.12306.cn/otn/resources/login.html',
            }
        },
        'captcha': {
            'url': r'https://kyfw.12306.cn/otn/passcodeNew/getPassCodeNew?module=login&rand=sjrand&rand=sjrand&{}'
                .format(random.random()),
            'method': 'GET',
            'response': 'binary',
        },
        'captchaCheck': {
            'url': r'https://kyfw.12306.cn/otn/passcodeNew/checkRandCodeAnsyn',
            'method': 'POST',
            'headers': {
                'Origin': r'https://kyfw.12306.cn',
                'Referer': r'https://kyfw.12306.cn/otn/leftTicket/init',
                'Content-Type': r'application/x-www-form-urlencoded; charset=UTF-8',
            }
        },
        'login': {
            'url': r'https://kyfw.12306.cn/otn/login/loginAysnSuggest',
            'method': 'POST',
            'headers': {
                'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
                'Origin': r'https://kyfw.12306.cn',
                'Referer': r'https://kyfw.12306.cn/otn/leftTicket/init',
            }
        },
        'loginOut': {
            'url': r'https://kyfw.12306.cn/otn/login/loginOut',
            'method': 'GET',
            'headers': {
                r'Content-Type': r'application/x-www-form-urlencoded',
                'Host': r'kyfw.12306.cn',
                'Referer': r'https://kyfw.12306.cn/otn/leftTicket/init',
            },
            'response': 'html',
        },
        "getDevicesId": {  # 获取用户信息
            "url": "https://kyfw.12306.cn/otn/HttpZF/logdevice?algID=7uavUD4Jd4&hashCode=HOZOxxdIBd2qLGoJqA0iStx-P1n86WFZ6Gds9U4-XyU&FMQw=1&q4f3=zh-CN&VPIf=1&custID=133&VEek=unknown&dzuS=0&yD16=0&EOQP=382b3eb7cfc5d30f1b59cb283d1acaf3&lEnu=3232235885&jp76=52d67b2a5aa5e031084733d5006cc664&hAqN=Linux%20x86_64&platform=WEB&ks0Q=d22ca0b81584fbea62237b14bd04c866&TeRS=1003x1920&tOHY=24xx1080x1920&Fvje=i1l1o1s1&q5aJ=-8&wNLf=99115dfb07133750ba677d055874de87&0aew=Mozilla/5.0%20(X11;%20Linux%20x86_64)%20AppleWebKit/537.36%20(KHTML,%20like%20Gecko)%20Chrome/75.0.3770.142%20Safari/537.36&E3gR=7484b4d443309cac29a8c080495fc1c0&timestamp=",
            "method": "GET",
            "Referer": "https://kyfw.12306.cn/otn/passport?redirect=/otn/",
            "Host": "kyfw.12306.cn",
        }
    },
}

autoVerifyUrls = {
    '12305':{
        'url':'https://kyfw.12306.cn/passport/captcha/captcha-image64?login_site=E&module=login&rand=sjrand&{0}'.format(
            int(time.time() * 1000)),
        'method':'GET',
        # 'response': 'html',
    },
    'api':{
        'url':'https://12306.jiedanba.cn/api/v2/getCheck',
        'method':'POST',
        'headers': {'Content-Type': 'application/json'}
    },
    'img_url':{
        'url':'https://check.huochepiao.360.cn/img_vcode',
        'method':'POST'
    },
    'check_url':{
        'url':'https://kyfw.12306.cn/passport/captcha/captcha-check',
        'method':'GET'
    },
    "origin_url":"https://12306.jiedanba.cn/"
}

queryUrls = {
    'query': {
        'url': r'https://kyfw.12306.cn/otn/leftTicket/query',
        'method': 'GET',
        'headers': {
            'Referer': r'https://kyfw.12306.cn/otn/leftTicket/init',
        }
    },
}

submitUrls = {
    'dc': {
        'submitOrderRequest': {
            'url': r'https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest',
            'method': 'POST',
            'headers': {
                'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init',
                'Content-Type': r'application/x-www-form-urlencoded; charset=UTF-8',
                'Host': r'kyfw.12306.cn',
                'X-Requested-With':'XMLHttpRequest',
                'Accept-Encoding':'gzip, deflate, br',
                'Accept-Language':'zh-CN,zh;q=0.9',
                'Origin':'https://kyfw.12306.cn',
            },
        },
        'getPassengerDTOs': {
            'url': r'https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs',
            'method': 'POST',
        },
        'getExtraInfo': {
            'url': r'https://kyfw.12306.cn/otn/confirmPassenger/initDc',
            'method': 'POST',
            'headers': {
                'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init',
                'Host': r'kyfw.12306.cn',
                'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            },
            'response': 'html',
        },
        'checkUser': {
            'url': r'https://kyfw.12306.cn/otn/login/checkUser',
            'method': 'POST',
            'headers': {
                'Referer': r'https://kyfw.12306.cn/otn/leftTicket/init',
                'Content-Type': r'application/x-www-form-urlencoded; charset=UTF-8',
            }
        },
        'checkOrderInfo': {
            'url': r'https://kyfw.12306.cn/otn/confirmPassenger/checkOrderInfo',
            'method': 'POST',
            'headers': {
                'Referer': r'https://kyfw.12306.cn/otn/confirmPassenger/initDc',
            },
        },
        'getQueueCount': {
            'url': r'https://kyfw.12306.cn/otn/confirmPassenger/getQueueCount',
            'method': 'POST',
            'headers': {
                'Referer': r'https://kyfw.12306.cn/otn/confirmPassenger/initDc',
            },
        },
        'confirmForQueue': {
            'url': r'https://kyfw.12306.cn/otn/confirmPassenger/confirmSingleForQueue',
            'method': 'POST',
            'headers': {
                'Referer': r'https://kyfw.12306.cn/otn/confirmPassenger/initDc',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            },
        },
        'queryOrderWaitTime': {
            'url': r'https://kyfw.12306.cn/otn/confirmPassenger/queryOrderWaitTime',
            'method': 'GET',
            'headers': {
                'Referer': r'https://kyfw.12306.cn/otn/confirmPassenger/initDc',
            },
        },
        'resultOrderForQueue': {
            'url': r'https://kyfw.12306.cn/otn/confirmPassenger/resultOrderForDcQueue',
            'method': 'POST',
            'headers': {
                'Referer': r'https://kyfw.12306.cn/otn/confirmPassenger/initDc',
            },
        },
        'queryMyOrderNoComplete': {
            'url': r'https://kyfw.12306.cn/otn/queryOrder/queryMyOrderNoComplete',
            'method': 'POST',
            'headers': {
                'Referer': r'https://kyfw.12306.cn/otn/queryOrder/initNoComplete',
            },
        }

    },
    'wc': {
        'submitOrderRequest': {
            'url': r'https://kyfw.12306.cn/otn/leftTicket/submitOrderRequest',
            'method': 'POST',
            'headers': {
                'Referer': 'https://kyfw.12306.cn/otn/leftTicket/init',
                'Content-Type': r'application/x-www-form-urlencoded; charset=UTF-8',
                'Host': r'kyfw.12306.cn',
                'X-Requested-With':'XMLHttpRequest'
            },
        },
        'getPassengerDTOs': {
            'url': r'https://kyfw.12306.cn/otn/confirmPassenger/getPassengerDTOs',
            'method': 'POST',
        },
        'getExtraInfo': {
            'url': r'https://kyfw.12306.cn/otn/confirmPassenger/initWc',
            'method': 'GET',
            'response': 'html',
        },
        'checkOrderInfo': {
            'url': r'https://kyfw.12306.cn/otn/confirmPassenger/checkOrderInfo',
            'method': 'POST',
            'headers': {
                'Referer': r'https://kyfw.12306.cn/otn/confirmPassenger/initWc',
            },
        },
        'checkUser': {
            'url': r'https://kyfw.12306.cn/otn/login/checkUser',
            'method': 'POST',
            'headers': {
                'Referer': r'https://kyfw.12306.cn/otn/leftTicket/init',
                'Content-Type': r'application/x-www-form-urlencoded; charset=UTF-8',
            }
        },
        'getQueueCount': {
            'url': r'https://kyfw.12306.cn/otn/confirmPassenger/getQueueCount',
            'method': 'POST',
            'headers': {
                'Referer': r'https://kyfw.12306.cn/otn/confirmPassenger/initWc',
            },
        },
        'confirmForQueue': {
            'url': r'https://kyfw.12306.cn/otn/confirmPassenger/confirmGoForQueue',
            'method': 'POST',
            'headers': {
                'Referer': r'https://kyfw.12306.cn/otn/confirmPassenger/initWc',
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            },
        },
        'queryOrderWaitTime': {
            'url': r'https://kyfw.12306.cn/otn/confirmPassenger/queryOrderWaitTime',
            'method': 'GET',
            'headers': {
                'Referer': r'https://kyfw.12306.cn/otn/confirmPassenger/initWc',
            },
        },
        'resultOrderForQueue': {
            'url': r'https://kyfw.12306.cn/otn/confirmPassenger/resultOrderForWcQueue',
            'method': 'POST',
            'headers': {
                'Referer': r'https://kyfw.12306.cn/otn/confirmPassenger/initWc',
            },
        },
        'queryMyOrderNoComplete': {
            'url': r'https://kyfw.12306.cn/otn/queryOrder/queryMyOrderNoComplete',
            'method': 'POST',
            'headers': {
                'Referer': r'https://kyfw.12306.cn/otn/queryOrder/initNoComplete',
            },
        }

    }
}

