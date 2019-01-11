
# pip: python install package,python包管理工具。安装python解释器时以自带。目录已添加到环境变量中。
# 包管理工具：包是别人写好的代码。经常有这种情况 ，比如爬虫框架功能的A包，里面引用了负责解析网页的B包，B包引用了更加基础底层的C包。包关系成树装引用。B包依赖C包。直接使用A包，运行报错缺少B包，确实依赖包。
# 为了解决依赖包的问题，包管理工具的出现，主要功能：管理、下载、上传包。解决依赖，安装一个包时会把相关的依赖包都安装好。
"""
 pypi: https//pypi.org/是查找、安装、发布python包的一个平台。pip工具默认从pypi下载包。
 pip list # 输出安装过的三方包的列表。
pip install 包名   # (常用）安装包。安装包的本质是从pypi下载，解压到C:\Python36\Lib\site-packages下，默认安装包的最新版本。
pip install requests==2.19.0  # 安装指定版本的包
pip uninstall 包名    # 卸载包

"""
"""
批量备份和安装
pip freeze > requirement.txt  # 将解释器中的包和版本导入到一个文件中
pip install > requirement.txt  # 根据requirement.txt的信息批量安装对应版本的包。

pip安装包慢的问题。


"""
"""
python虚拟解释器环境。
场景：公司不同时期的多个开发项目，使用的python大版本和各个版本不尽相同。每个项目要求有一套让自己成功运行的解释器。一个程序员可能同时开发多个项目。电脑上需要有多套python解释器项目一一对应。
解决：我们电脑现在只有一套python解释器，以它为基础，虚拟出几个解释器的组合。老的教材中要先安装virtualenv（虚拟environment环境），因为使用较多，所以py3.4起官方直接内置了venv包

"""

"""
(cmd)python -m venv 虚拟环境名     # 创建虚拟环境
创建完发现虚拟环境具备python.exe pip.exe active.bat，Lib库中除了pip包是空的，就好像刚重装完电脑系统。
cd aaa/Scripts
activate.bat     # 激活虚拟环境
虚拟环境可以实现项目隔离，不怕出





"""


"""
另外安装方法：
1. 源码安装。从github包的主页/releases 找到source code。解压。cd到解压后的包根目录。
python setup.py install
优点： 适合任何文件操作系统和python版本。缺点： 有些包源代码调用了c++代码，但本机没有c++编译器，编译报错。
2. wheel文件安装。wheel文件时有人已经安装好c++编译器，根据操作系统和python版本编译器好这种平台上可运行的二进制pip上安装的包，实际上就是平台为我们准备好的适合当前操作系统和python版本的.wheel文件
pypi上查找下载对应版本的.wheel文件
pip install requests_x64_win_p36.whl
优点不会报错
3 pip install 包名





"""











