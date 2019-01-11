# import os
# from os import path, open
# # from os import *
# #
import requests
from lxml import etree
import os
import time
# # url = 'http://www.ivsky.com/tupian/yueliang_v49822/'
# url = 'http://www.ivsky.com/tupian/'
# resp = requests.get(url)
#
# html_content = resp.text
# html_dom = etree.HTML(html_content)
# # print(html_content)
# # pattern_img_src = '//ul[@class="pli"]/li/div/a/img/@src'
# # img_src_list = html_dom.xpath(pattern_img_src)
# y1 = '//ul[@class="ali"]/li/div/a/@title'
# y2 = html_dom.xpath(y1)
# print(y2)
def z1(url_1):
    resp = requests.get(url_1)
    html_content = resp.text
    html_dom = etree.HTML(html_content)
    # pattern_img_src = '//ul[@class="pli"]/li/div/a/img/@src'
    pattern_img_src = '////ul[@class="ali"]/li/p/a/@href'
    v1 = html_dom.xpath(pattern_img_src)
    y1 = '////ul[@class="ali"]/li/p/a/@title'
    y2 = html_dom.xpath(y1)
    print(v1)
    print(y2)

    for i in v1:
        print(i)
        url_3 = 'http://www.ivsky.com'+i
        print(url_3)
        resp = requests.get(url_3)
        html_content = resp.text
        html_dom = etree.HTML(html_content)

        # pattern_img_src = '//ul[@class="pli"]/li/div/a/img/@src'
        pattern_img_src = '////ul[@class="pli"]/li/div/a/img/@src'
        v2 = html_dom.xpath(pattern_img_src)
        print(v2)

        for index,img_src_url in enumerate(v2):
            resp = requests.get(img_src_url, timeout=10)
            if resp.status_code !=200:
                raise Exception("图片请求失败")
            n3 = resp.content
            # print(n3)
            y1 = str(index)

            for i_1 in y2:
                print(i_1)
                n1 = os.path.exists('D:\\testimg\\' + i_1)

                if n1 == False:
                    # os.mkdir('D:\\testimg')
                    os.mkdir('D:\\testimg\\' + i_1)
                n4 =   y1 + '.jpg'
                i_2 = (i_1+'\\'+n4)
                print('D:\\testimg\\'+i_2)

                with open('D:\\testimg\\'+i_2,'ab') as file:
                    file.write(n3)
                    print('正在生成第',index,'张图片')
                    print('成功')






if __name__ == '__main__':
    print(z1('http://www.ivsky.com/tupian/'))