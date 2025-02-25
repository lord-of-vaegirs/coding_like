"""
python支持函数有多返回值
return之后几个返回值之间用逗号隔开
接收时也用逗号隔开变量来接收

传入参数的四种使用方式：
1.位置参数 传参的时候位置和个数保持一致
2.关键字传参 key=value形式传入参数 消除了顺序要求 更精确了
位置参数和关键字参数可以混用，但位置参数得放在前面
3.缺省参数 默认参数 在函数定义时就规定了其默认值，无传入值的时候用默认值，且位置必须在位置参数之后
4.不定长参数 不确定参数个数时使用
4.1 位置传递 利用*参数可以将传入的参数收入一个参数变量中，合并为元组类型
4.2 关键字传递 利用**参数可以传入key=value形式的参数，放入dict中

参数传递
参数不仅仅可以是数据，也可以是新的函数
所以，传入的是代码的执行逻辑
普通的函数传入数据，计算逻辑确定，数据不确定
传入函数的函数计算逻辑不确定，但是数据需要确定

匿名函数 lambda
def定义有名称的函数
lambda定义匿名函数
有名称的函数可以重复使用
匿名函数只能用一次
lambda 传入参数：函数体（一行代码）
"""
def func():
    return 1,2

x,y=func()
print(f"{x},{y}")

def func2(x,y,z,w):
    result=x+y+z+w
    print(f"{x},{y},{z},{w}")
    return result

print(f"{func2(w=12,x=23,z=24,y=100)}")

def func3(gender,age,name="bob"):
    return gender,age,name

gen,ag,name=func3("boy",age=12)
print(f"{gen},{ag},{name}")

def func4(*arg):
    print(arg)

func4('python',3,56)

def func5(**kwargs):
    print(kwargs)

func5(name='python',age=12,score=100)

def addi(compute):
    result=compute(int(input()),int(input()))
    return result

def compute(x,y):
    return x*y

zz=addi(compute)
print(zz)

def test_func(compute):
    result = compute(1,2)
    print(result)

test_func(lambda x,y:x+y)
# lambda在写的时候已经定义好了，冒号后就是它的计算逻辑，不用return
# lambda只能用一次，下次用要重新写






