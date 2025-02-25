"""
异常处理（捕获异常）：
对bug适当提醒，整个程序继续进行

捕获常规（所有）异常：
try:
    可能发生错误的代码
except:
    如果出现异常执行的代码

捕获指定异常：
try:
    可能发生变量名未定义错误的代码
except NameError as e:
    如果出现异常执行的代码
    print(e) e就是异常信息

捕获多个异常：
try:
    可能发生错误的代码
except(error1,error2,...) as e:
    出现异常执行的代码
把多个error以元组的形式组合

捕获全部异常：
try:
    可能发生错误的代码
except Exception as e:
    出现异常执行的代码

else：
没有出现异常时执行else里面的语句

finally：
无论出现异常与否都要执行的语句
"""
try:
    f=open("test03.txt","r")
except Exception as e:
    f=open("test03.txt","a",encoding="UTF-8")
    f.write("none")
else:
    for i in f:
        print(f"{f.readline()}")
finally:
    f.close()

"""
异常具有传递性
在函数之间传递
如果异常在一层函数中没能被捕获
就会传到上一层的函数中去，最终被最上面一层函数捕获
"""
def func3():
    num=1/0
def func2():
    func3()
def func1():
    try:
        func2()
    except Exception as e:
        print(e)
func1()













