
# pillow例子2 随机生成验证码

from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random


# 随机字母
def n5():
    return chr(random.randint(65, 90))


def n():
    pass

# 随机数字


def n3():
    return random.randint(0, 30)

# 随机字体颜色 稍深


def n2():
    return (random.randint(10, 80), random.randint(10, 80), random.randint(10, 80))

# 随机生成背景颜色


def n4():
    return (random.randint(90, 150), random.randint(90, 150), random.randint(90, 150))


# 生成空白背景图层

image = Image.new('RGB', size=(240, 60), color=(204, 153, 0))    # 色彩模式   大小
# 生成绘制对象
draw = ImageDraw.Draw(image)
# 字体对象， 字体， 字号
font = ImageFont.truetype('arial.ttf', 36)


# 循环像素点并填充颜色
for x in range(1, 241):
    for y in range(1, 61):
        draw.point(xy=(x, y), fill=n4())


# 随机生成位置
def n7():
    return (random.randint(0,25))

# 随机生成干扰线


def n8():
    pic_size = (240, 60)
    line_color = (230, 0, 0)
    begin = (random.randint(0, pic_size[0]), random.randint(0, pic_size[1]))
    end = (random.randint(0, pic_size[0]), random.randint(0, pic_size[1]))
    draw.line([begin, end], fill=line_color)


for i in range(3):
    n8()


# 生成文字

for t in range(0, 4):
    draw.text((60*t+n7(), n7()), n5(), font=font, fill=n2())


# 加模糊滤镜
# image = image.filter(ImageFilter.BLUR)
# 加扭曲
# params = [1 - float(random.randint(1, 2)) / 100,
#           0,
#           0,
#           0,
#           1 - float(random.randint(1, 10)) / 100,
#           float(random.randint(1, 2)) / 500,
#           0.001,
#           float(random.randint(1, 2)) / 500
#           ]
# size=(240,60)
# image = image.transform(size, Image.PERSPECTIVE, params)
# 保存
image.save('n1.jpg', 'jpeg')

# 作业：追加需求
"""
1.在github上搜索关键字“生成验证码”，查看学习别人生成验证码的流程。拷贝一份别人的实现并成功运行。
2. 绘制文字时y坐标更加凌乱(百度搜索‘验证码’）
3. 添加干扰斜线或曲线
4.文字扭曲效果，猜测跟滤镜相关，百度‘pillow滤镜文字扭曲’
5. 背景干扰点
6. 文字味中味。
7. 字体粗细、大小混排
8. 文字轻度旋转
9. 把一张风景图作为验证码的背景。


"""



