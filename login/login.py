from PIL import Image
import requests
from json import loads
class Login(object):

    def __init__(self):
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                                    "Chrome/75.0.3770.142 Safari/537.36"}
        self.session = requests.session()

    def get_img(self):
        url = "https://kyfw.12306.cn/passport/captcha/captcha-image?login_site=E&module=login&rand=sjrand"
        reponse = self.session.get(url=url, headers=self.headers, verify=False)
        with open('img.jpg','wp') as f
            f.write(reponse.content)
        im = Image.open('img.jpg')
        im.show()
        im.close()
        _answer = input("请输入验证码位置（以，隔开）：")
        return _answer

    def captcha_answer(self,_answer):
        use_ans = _answer.split(',')
        true_ans = ['35,35','105,35','175,35','245,35','35,105','105,105','175,105','245,105']
        use_ans_list = []
        for item in use_ans:
            use_ans_list.append(true_ans[int(item)])
        use_ans_list_str = ','.join(use_ans_list)
        return use_ans_list_str

    def captcha_check(self, captcha_answer):
        checkurl = "https: // kyfw.12306.cn/passport/captcha/captcha-check?rand=sjrand&login_site =E&answer =" \
                   + captcha_answer.unicode()
        cont = self.session.get(url=checkurl, headers=self.headers, verify=False)
        dic = loads(cont.content.decode())
        answer_code = dic['result_code']
        if answer_code == 4:
            return True
        else:
            return False

    def login(self,captcha_answer):
        user_name = input("请输入用户名：")
        password = input("请输入密码:")
        loginurl = "https://kyfw.12306.cn/passport/web/login"
        date = {
            'username':user_name,
            'password':password,
            'appid':'otn',
            'answer':captcha_answer,
           }
        result = self.session.post(url=loginurl, headers=self.headers, date=date, verify=False)
        get_result = loads(result.content.decode())
        fin_result = get_result['result_message']
        if fin_result == "登陆成功":
            print("恭喜登陆成功")
        else:
            print("登陆失败")
    if _name_ == '_main_':
        login = Login()
        img = get_img(login)
        answer = captcha_answer(img)
        chek = False
        while not chek:
            chek = captcha_check(answer)
            if chek:
                print("验证通过")
            else:
                print("验证失败")
        Login.login()


