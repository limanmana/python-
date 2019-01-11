import os
import time
import datetime
from datetime import datetime, timedelta
def reName(y1):
    for category in os.listdir(y1):
        n1 = os.path.join(y1, category)
        print(n1)
        if not os.path.isdir(n1):
            continue
        y3 = os.listdir(n1)
        n2 = '时间戳_'
        z2 = 0
        for y2 in y3:
            print('正在处理' + category + '分类下的' + y2)
            n3 = os.path.join(n1, y2)
            z2 = z2 + 1
            # n3 = os.path.splitext(y2)[0]
            z1 = '.jpg'                   # 扩展名修改
            # t = os.path.getctime(n3)

            y3 = os.path.join(n1,'1.jpg')

            os.rename(n3, y3)
if __name__ == '__main__':
        y1 = 'D:\windows聚焦'
        reName(y1)





