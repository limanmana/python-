# random 随机
import random

# 0到1之间生成一个随机数，
print(random.random())  # 0到1之间生成一个随机数

# 随机数如何产生：cpu主频，cpu温度，鼠标滑动轨迹 等等。

# randint() 起止范围内的随机整数，左闭右开区间。
print(random.randint(1, 50))

# choice 从可迭代对象中随机选一个元素
print(random.choice(['小明', '小红', '小王', '小李']))

# shuffle 洗牌
list1 = [1, 2, 3, 4]
random.shuffle(list1)
print(list1)


