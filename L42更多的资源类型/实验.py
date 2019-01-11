import requests
from lxml import etree

login_url = 'https://github.com/login'
do_login_url = 'https://github.com/session'
profile_url = 'https://github.com/settings/profile'

# 未登录时请求个人页，会重定向，返回index登录表单html数据。
# profile_resp = requests.get(profile_url)
# print(profile_resp.status_code, profile_resp.text)

# 伪造headers
headers = {
    'Host': 'github.com',
    'Referer': 'https://github.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}

# requests Session会话。优点：1保持会话，管理cookie 2重用底层tcp连接同一网址提升效率。
s = requests.Session()
login_resp = s.get(login_url, headers=headers)
if login_resp.status_code != 200:
    raise Exception("get请求登录页表单失败{}".format(login_resp.status_code))
login_html_content = login_resp.text

# 获取表单的csrf token
login_dom = etree.HTML(login_html_content)
pattern_authenticity_token = '//input[@name="authenticity_token"]/@value'
authenticity_token = login_dom.xpath(pattern_authenticity_token)[0]
print('表单csrf token', authenticity_token)

# 请求登录接口
session_args = {    # 准备所需参数
    'commit': 'Sign in',
    'utf8': '✓',
    'authenticity_token': authenticity_token,
    'login': 'r1325913569@163.com',
    'password': 'r1325913569'
}
session_resp = s.post(do_login_url, headers=headers, data=session_args)
if session_resp.status_code != 200:
    raise Exception("请求登录接口失败{}".format(session_resp.status_code))
print("登录成功")
# 请求成功后 会话id user_session会写入到requests的cookie管理器中，以后的请求会携带上，从而保持登录状态
print('登录后cookie', session_resp.cookies)

# 请求个人设置页
profile_resp = s.get(profile_url, headers=headers)
if profile_resp.status_code != requests.codes.ok:
    raise Exception("请求个人设置页失败")
# print(profile_resp.text)
# 获取邮箱
# 账户名登录的 select标签id和邮箱登录的不一致，根据变化自己修改
pattern_profile_email = '//select[@id="user_profile_email"]/option[2]/text()'
profile_dom = etree.HTML(profile_resp.text)
profile_email = profile_dom.xpath(pattern_profile_email)[0]
print('最终信息', profile_email)