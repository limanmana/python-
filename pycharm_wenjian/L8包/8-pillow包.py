# pillow包 (图像处理)
# pillow ：PIL（python image library）是一个有关图像图片处理的包，这个包底层用的C++，但PIL包是python2下使用。所以又更新了一个适合python3的版本的、基于PIL包的新包pillow。


from PIL import Image, ImageFilter

im = Image.open('demo.jpg')
print(im.size)
width, height = im.size
print(width, height)


# 缩放
im.thumbnail((500, 500))
# 保存为新图片
im.save('demo2.jpg', 'jpeg')
# 旋转
im2 = im.rotate(0)
im2.show()   # 临时打开
# 滤镜
im3 = im.filter(ImageFilter.BLUR)   # （图像模糊）
im3.show()

