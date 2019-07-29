import requests
from PIL import Image
from json import loads
import urllib3
urllib3.disable_warnings()


class Login(object):
    def __init__(self):
        self.headers = {
            'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'
        }
        self.session = requests.session()

    def get_img(self):
        url = 'https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand'
        response = self.session.get(url, headers=self.headers, verify=False)
        with open('captcha.jpg', 'wb') as f:
            f.write(response.content)
        try:
            img = Image.open('img.jpg')
            img.show()
            img.close() 
        except IOError:
            print("请输入验证码")
        else:
            print("请输入验证码")


        captcha_solution = input("请输入验证码位置，以','分割:")
        return captcha_solution

    def captcha_answer(self, captcha_solution):
        solution = ['35,35', '105,35', '175,35', '245,35', '35,105', '105,105', '175,105', '245,105']
        ans_list = captcha_solution.split(',')
        captcha_list = []
        for i in ans_list:
            captcha_list.append(solution[int(i)])
        captcha_answer = ','.join(captcha_list)
        return captcha_answer

    def captcha_check(self, captcha_answer):
        captcha_check_url = 'https://kyfw.12306.cn/passport/captcha/captcha-check?&rand=sjrand&answer=' \
                            + captcha_answer.unicode()
        captcha_result = self.session.get(captcha_check_url, headers=self.headers, verify=False)
        captcha_dic = loads(captcha_result.content.decode())
        captcha_code = captcha_dic['result_code']
        # 取出验证结果:4：成功 5：验证失败 7：过期 8：信息为空
        if str(captcha_code) == '4':
            return True
        else:
            return False

    def login(self, captcha_answer):
        username = 'wyq3005'
        password = 'Mm123456'
        login_url = "https://kyfw.12306.cn/passport/web/login"
        data = {
            'username': username,
            'password': password,
            'appid': 'excater',
            'answer': captcha_answer
        }
        login_result = self.session.post(url=login_url, data=data, headers=self.headers, verify=False)
        login_dic = loads(login_result.content.decode())
        login_msg = login_dic['result_message']
        # 结果的编码方式是Unicode编码，所以对比的时候字符串前面加u,或者mes.encode('utf-8') == '登录成功'进行判断，否则报错
        if login_msg.encode('utf-8') == '登录成功':
            print('恭喜你，登录成功，可以购票!')
        else:
            print('对不起，登录失败')


if __name__ == '__main__':
    login = Login()
    cs = login.get_img()
    ca = login.captcha_answer(cs)
    check = False
    # 只有验证成功后才能执行登录操作
    while not check:
        check = login.captcha_check(ca)
        if check:
            print('验证通过!')
        else:
            print('验证失败，请重新验证!')
