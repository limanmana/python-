# GUI
# GUI: graphic User Interface,图形用户界面。我们平时用的qq、pycharm这些软件的界面都叫GUI开发。因为GUI相关库生态不统一、学习成本低、功能等方面没有HTML强大,目前开发者不多。
# windows上的软件底层调动的是C++ directX 底层图形接口。其他语言的开发者封装win底层图形接口形成自己语言可以调用的图形库。

from tkinter import Tk, Listbox

# import tkinter
root = Tk()
list1 = ['hello word']
list2 = ['人生苦短，我用python']
# 创建两个列表组件
com_a = Listbox(root)
com_b = Listbox(root)


# 往列表组件写数据
for i in list1:
    com_a.insert(0, i)
for i in list2:
    com_a.insert(1, i)


# 将com_a部件放置到主窗口中
com_a.pack()
com_b.pack()


# 进入消息循环、事件监听
root.mainloop()













