# # 时间处理   time   datetime
import time
import datetime
from datetime import datetime,timedelta



from datetime import datetime, timedelta    # 从datetime包引入datetime

# 1 datetime.now()返回当前时间datetime.datetime(2018, 10, 24, 15, 17, 12, 684304)对象。方便进行日期加减等处理。
print(datetime.now())

# 2 创建datetime对象
dt = datetime(2018, 10, 24, 15, 21, 45)
print(dt.year)   # 年
print(dt.month)  # 月

# 3 日期加减  场景： 判断活动截止；定时任务
print(datetime.now() + timedelta(days=-1, hours=10))

# 4 (常用)格式化输出 strftime  format   对象转字符串
print(datetime.now().strftime('%Y/%m/%d %H:%M:%S'))    # 2018/10/24 15:34:13
# %Y  %y  year  年
# %m  month  月
# %d  day  日
# %H  hour 小时
# %M  minute 分钟
# %S  seconds 秒
#  5>时间戳转datetime对象
print(datetime.fromtimestamp(1540368793))
#  6>字符串转时间对象
dtstr = '2018-10-28T20:11:58.214Z'
dt = datetime.strptime(dtstr, '%Y-%m-%dT%H:%M:%S.%fZ')
print(dt)



import time
# 1> (常用)生成当前时间的时间戳  time()
# 时间戳 timestamp: 当前时间 减去 1970-1-1 0:0:0的秒数。把时间量化成数字，比较时间先后顺序，计算转换有优势，缺点可读性差，默认长度只能表示到2030年
print(time.time())

# 2> 生成本地时间  返回结构化时间
print(time.localtime())


# 3>  (常用)格式化时间
print(time.strftime('%Y/%m/%d %H:%M:%S', time.localtime()))

# 4> 字符串转time结构
n = time.strptime('2018-10-28T20:11:58.214Z', '%Y-%m-%dT%H:%M:%S.%fZ')
print(n)
#
# 5> 从time结构对象生成数字时间戳  make
print(time.mktime(n))

# 6>time   场景：操作温度传感器，每5s打印一次数据
time.sleep(5)  #
