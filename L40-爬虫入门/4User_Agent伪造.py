# User_Agent伪造
# User_Agent: request_heads请求中的一个字段，包好操作系统和浏览器信息。
# 如果来自同一个User_Agent的请求过于频繁，服务器可能封停。所以我们要伪造User_Agent信息。
import random
def grt_randm_user_agent():
    user_agent_list = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
    ]
    return random.choice(user_agent_list)


# print(grt_randm_user_agent())
user_agent = grt_randm_user_agent()


# import urllib.request
# req = urllib.request.Request('https://www.baidu.com',data={'wd':'python'})
# req.add_header('User_Agent',user_agent)
# resp = urllib.request.urlopen(req)
# print(resp)
# html =
import random
from fake_useragent import UserAgent
ua = UserAgent()
print(ua.random)
