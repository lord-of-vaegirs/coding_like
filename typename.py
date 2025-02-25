"""
这里写文件的解释

"""
print(666)
print(13.14)
print("hello")
# 单行注释用# 号
"""
多行注释用三个双引号
用于文件和类和对象进行解释
"""
# int float bool complex tuple string list set 都是数据类型
# 定义变量 变量名=值 即可
money=50
pay=0
print("钱有",money)
money-=10
# py += -= 计算也适用
print("钱有",money)
# print可以往其中放无限个输出
# type()查看数据类型
print(type(money)) # 直接查看
_type=type(money)
print(_type) # 赋给变量再输出
div=type(888)
print(div)
# python里面变量没有数据类型！！！只是存储了对应的数据，才让其有了类型！
# 数据类型转换 _type(x) 即为把x转化为_type类型的数据
# int(x) float(x) str(x)
num=str(11)
print(type(num),num)
# 万物皆可转换成字符串 但反向不一定
print(int(11.94))
# 浮点数转整数会直接抛掉小数点之后的数字
# 名字就叫标识符 只能用英文 数字 下划线 不能以数字开头
# 关键字不能占用
# py大小写敏感
# + - * / //（取整除）% **（乘方）
# += -= *= /= %= **= //=
num1=10
num2=20
num=((num1+num2)//2)**3
print(num)
"""
字符串定义:
单引号定义（里面可以用双引号
双引号定义（里面可以用单引号
多引号定义
\' \" 可以解除引号效用
"""
name='lixingjian'
name2="\nlixingjian"
name3="""
lixingjian
"""
print(name,name2,name3)
# 拼接字符串
# 使用+拼接字符串
using="abc"
usine="def"
print(using+usine)
# 拼接只能适用于字符串
"""
字符串格式化
% 占位符
s 表示要让变量占位的地方
e.x.p：
name="nihao"
message="woshi %s" % name
print(message)
"""
name="nihao"
message="woshi %s" % name
print(message)
"""
其他类型的数据也可以通过这种占位的方式
拼接入字符串
多个数据拼接时，用(,)
顺序要对应
"""
class_salary=123
avg_salary=147.124
option="qwertyu %d : %.3f" % (class_salary,avg_salary)
print(option)
"""
%d 占位整型
%f 占位浮点型 
%s 占位字符串
数字精度控制 m.n
m设置宽度 n控制小数点后位数 小数点后也会算入宽度
会四舍五入 m如果小于数字本身的宽度，不会生效
"""
a1=12.345
print("%5.3f" % a1)
"""
快速格式化
f"内容{变量}"
但是没法控制精度
不管类型
"""
a2=123
a3=34.56
print(f" {a2} , {a3} ")
"""
对表达式进行格式化
表达式：有执行结果的代码语句
只需把上面格式化里面的放置变量的地方全都换成表达式即可
"""
print("%d" % (1+2))
print("%s" % type(2+3))
print(f"{1+2}")
"""
输入input
name=input()
无论输入什么，都默认为字符串类型
必须自行类型转换
"""
opm=input("请告诉我\n")
print(f"{opm}")
print(f"{type(opm)}")





