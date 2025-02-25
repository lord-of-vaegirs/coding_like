# len()是内置的函数 用于计算字符串长度
str1="hello"
print(f"{len(str1)}")
"""
函数的定义
def 函数名（传入参数）:
    函数体
    return 返回值
参数和返回值不是必须，可以先省略
"""
def say_hi():
    print("hello!")

# 调用函数 函数名（）
say_hi()
# 带传入参数的函数
x = input("输入x")
x=int(x)
y=input("输入y")
y=int(y)
def say_hi2(x,y):
    num2=x+y
    print(f"{num2}")
say_hi2(x,y)
# 带返回值的函数
def say_hi3(x,y):
    num3=x+y
    return num3 # return 是函数定义里面最后的一句 之后的语句不再会被执行
r=say_hi3(x,y)
print(r)
# 没有返回值的函数返回的是 None 类型是 Nonetype
print(type(None))
# None在if判断中代表False
def check_age(x):
    """
    用于检查年龄
    :param x: 传入的年龄
    :return: 返回年龄或none
    """
    if x>18 :
        return x
    else :
        return None
result=check_age(16)
if not result:
    print("NONE")
# 嵌套调用函数
def func1():
    print("hello")
def func2():
    func1()
func2()
# 全局变量定义在函数体和循环体外
# 局部变量定义在局部作用域内
# 在局部作用域内定义变量时，加一个global 就可以让他成为全局变量
def add(x,y):
    global addi
    addi=x+y

add(x,y)
print(addi)

money=5000000
name=input("用户姓名: ")
def check_account():
    print(f"账户余额：{money}")

def saving(x):
    global money
    money+=x
    print(f"已存款{x}元")


def taken(x) :
    global money
    money-=x
    print(f"已取款{x}元")


def main_menu():
    print(f"请选择需要的服务\t")
    print(f"1 查询余额\t")
    print(f"2 存入\t")
    print(f"3 取出\t")
    print(f"4 退出\t")
    sgn=int(input())

    if sgn==1 :
        check_account()
        return 1
    elif sgn==2 :
        saving(int(input("请输入存入金额：")))
        check_account()
        return 2
    elif sgn==3 :
        taken(int(input("请输入取款金额：")))
        check_account()
        return 3
    else :
        print("已退出")
        return 4
flag=True
while flag :
    i=main_menu()
    if i==4 :
        break





