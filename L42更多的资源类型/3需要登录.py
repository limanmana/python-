要登录的情况
"""
场景：个人信息页，订单页，需要登录权限验证后才可以访问。
权限验证：网站通过token或sessionid来限制页面访问。
sessionid: http无状态，http://www.baidu.com?kw=python,这个请求只包含目的地址和参数，不包含登录信息。 登录后只能保证本次请求，下一次请求服务器仍然不知道是否用户是否登录。为了解决用户登录后会话保持问题，
解决方式：用户登录，服务器接收用户名密码验证，通过则根据用户信息生成摘要字符串，即token或sessionid，返回响应 告诉客户端保存token到cookie，浏览器接收响应后存储token到cookie。然后之后的每一次请求都会携带cookie，这样服务器就能认识客户端了。 cookie好像额外的参数。token好像婚礼的请帖。
"""

"""
需求：模拟登陆，获取github 个人页/emails/  登陆邮箱。

分析：直接访问个人页会重定向到登陆页。
1. 请求登录页， 接收sessionid存入cookie
1）先通过谷歌开发者工具找到login的请求（类型、url、参数）。刷新登录页，然后clear请求，然后点击登录，观察新出现的请求。
点击登录后发现https://github.com/session请求，302重定向，为了防止重定向后控制台信息被刷新掉，勾选开发者工具中的preserve log（页面重定向时保留日志不刷新）。
2）分析去登录这个请求。
路由，https://github.com/session 
方法，post
参数，commit: Sign in
    utf8: ✓
    authenticity_token: SbXCFPbfNbNPNW...
    login: 969501808@qq.com
    password: xxxx
    注意authenticity_token跟cookie中的user_sesssion不一样。authenticity_token是请求http://github/login登录页时的CSRF token，为了防止表单传出过程中被截取伪造。
    user_sesssion是登录成功后服务器返回的token，代表已经登录。
2. 请求个人页（携带cookie）
3. 请求个人页（requests请求个人页成功后才发现），github个人设置页是返回完整的html，左边的菜单配合js每次只显示网页的一部分其余的隐藏。

梳理步骤：
1. get请求 login页面  
2. xpath把login页面authenticity_token获取下来，获取cookie
3. 去登录，准备好各个参数。
4. post请求 去登录  session 第3步的参数 cookie
5. get请求 个人页
6. xpath个人页邮箱给取出


小技巧：请求获取到的源代码粘贴到空的html文件去观察，利用pycharm自动格式化和搜索，观察写xpath。

"""
import requests
from lxml import etree

login_url = 'https://github.com/login'
do_login_url = 'https://github.com/session'
profile_url = 'https://github.com/se·2··ttings/profile'

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