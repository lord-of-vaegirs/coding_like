"""
numpy

官网：  www.numpy.org

numpy里面的+ - * / 有广播属性
两个数组相加 对应元素相加
其他同理

arr.shape 查看数组形状

np.reshape() 改变数组形状

np.transpose() 数组矩阵转置

np.dot() 点乘

np.mean(arr) 或者是 arr.mean() 求数组平均值

& 按位与 每一位做 and 运算

｜ 按位或 每一位做 or 运算

"""


import numpy as np

# array
# array数组
# 可以进行切片操作 [a:b:step] a的起点 b的终点（不包含）step为步长
# 如果是一维数组 切片功能同list
# 如果是二维数组 [a]索引一行 [a:b]索引a-b行 [a][b]索引二维数组元素
# arr[条件式] 这样的索引方式自带筛选机制 条件式符合才会通过索引

lt=[]

for i in range(15):
    a=10*np.random.rand()
    if len(lt)==0:
        lt=[a]
    else:
        lt.append(a)



for i in range(3):
    arr = lt[i:i + 5]
    if i==0 :
        A=np.array(arr)
    else:
        B=np.array(arr)
        A=np.hstack((A,B))

A=np.reshape(A,(3,5))

print(A)

C=10*np.random.rand(4,4)

D=C[C<10]
D=np.reshape(D,(4,4))
print(D)

np.random.seed(1) # 固定随机数种子 使得每一次的随机数固定

a=np.random.rand()

print(a)


barr=np.random.randint(0,100,(4,4))
s=np.sum(barr)
barr=barr[barr<=10]
print(f"{s},{barr}")










