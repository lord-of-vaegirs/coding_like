"""
module模块
是一个py文件
能定义函数、类和变量
里面包含可执行代码
快速实现一些功能 是一个工具包

模块的导入
[from 模块名] import [模块｜类｜变量｜函数｜*] [as 别名]
常见的组合形式：
import 模块名
from 模块名 import 类、变量、方法
from 模块名 import *
import 模块名 as 别名
from 模块名 import 功能名 as 别名

"""

"""
import time # 导入time.py这个文件
time.sleep(100) # 暂停100秒
"""


"""
from 模块名 import 功能名
这种导入方式只导入了特定的功能
"""
# from time import sleep
# sleep(100)
# 这个时候直接用sleep就行

"""
from 模块名 import * 
这种也是导入模块所有的功能
但是使用其中的功能不需要打模块名了
"""
# from time import *
# sleep(100)

"""
import 模块名 as 别名
from 模块名 import 功能名 as 别名
as可以给模块改名
也可以给模块内功能改名
"""

# t.sleep(5)
print("python")

# sp(5)
print("java")

# import模块的语句都写在文件开头就好了

"""
自定义模块
自己写一个python文件
内部写一些函数作为方法
在其他文件里面可以导入它作为模块
使用里面的功能

"""
from test_package1 import addi as a
result=a(12,34)
print(f"{result}")

# 若导入的两个模块里面都有某个同名功能，后导入的会覆盖掉前导入的功能
from test_package1.subs import addi as a
res=a(12,34)
print(f"{res}")

"""
测试模块
实际开发中，为了测试模块的效果，会在模块文件里写调用测试
这个时候，无论是在模块文件打开，还是进到程序里面导入模块打开，都会执行测试调用
为了避免这一情况
只需在模块文件里
if __name__=='__main__':
    func()
即可 
__name__是自带变量
在本文件中运行时值为__main__
其他地方运行都不是
实现了测试代码不会在正式程序里运行
"""

"""
__all__变量
有了all，就由他来规定谁是算在全部功能内的，否则默认所有功能
影响*的功能判定
__all__=['test_func1']
def test_func1():
def test_func2():
这个时候导入时用*，只能用test_func1()
"""
from test_package1.subs import *
t1()
t2()



"""
pip 包管理工具
提供了对python包的查找、下载、安装和卸载

pip --version 查找版本
pip install some-package-name 安装包
pip uninstall some-package-name 卸载包
pip list 查看已经安装的库

重要的三个库

numpy 数据计算

pandas 表格库

matplotlib 绘图库

"""
