# while 循环 while 判断语句 ：
# 缩进代表所属
lov=1
while lov<100 :
    lov+=1
print("end")
# while循环嵌套
num=0
while lov<1000 :
    num=0
    while num<100 :
        num+=1
        lov+=1
    lov+=10
print (f"{lov}")

"""
for循环在一个范围range内循环
范围由你来定
还设一个临时变量
range算一种序列类型
"""
range1="abcdefghijkmnopqrstuvwxyz"
for i in range1:
    print(i)
p=range(5) # 构建一个0 1 2 3 4的序列
for i in p:
    print("hello")
# range(num1,num2,step) num1为序列初始数，num2为序列结束位置但不包括它本身，step为步长
# range(num1,num2)
for i in range(101):
    print(i)
# 嵌套循环
for i in range(1,10):
    for j in range(1,i+1):
        print(f"{j}*{i}={j*i}\t",end=' ') # end=' ' 可以让每次输出结束的换行操作换成空格操作
    print() # 换行
# continue 停止当前循环并进行下一次循环
# break 终止当前循环，退出循环
# \t水平制表符可以对齐

account=10000
for i in range(1,21):
    import random
    num = random.randint(1, 10)
    if account<=0 :
        print("账户无余额")
        break
    if num<5 :
        print(f"{i}员工无工资")
    else:
        if account>=1000 :
            account-=1000
            print(f"{i}员工领取1000元，账户还剩{account}元")
        else :
            print(f"{i}员工领取{account}元，账户还剩0元")
            account = 0
