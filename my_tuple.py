"""
tuple元组
‘只读版’list
一旦定义完成，便不可修改
元组使用（）
用逗号隔开各个元素 数据可以是不同的数据类型
(ele1,ele2,ele3,...)
var=(ele1,ele2,ele3,...)
var=tuple()
"""
t1=(1,"python",False)
t2=()
t3=tuple()
print(t1)
print(t2)
print(t3)
print(type(t1))
t4=("hello",)
print(type(t4)) # 单个元素如果之后不写逗号，会被认为是单个元素对应的类型
# tuple也支持嵌套
tup1=(t1,t2,t3,t4)
print(tup1[0][1])
# 下标索引tuple当然支持


"""
1.index()
tuple.index(ele)

2.count()
tuple.count(ele)

3.len()
len(tuple)

三个功能都可用变量来接收

"""
x=t1.index(1)
y=t1.count("python")
z=len(t1)
print(x,y,z)

# tuple的循环遍历语法与list类似
id=0
while id<len(t1) :
    print(t1[id])
    id+=1

for i in range(len(t1)):
    print(t1[i])

"""
tuple 特点
可以容纳多个元素 
可以容纳不同类型的元素
数据有序储存
允许重复元素存在
不可以修改元素
但可以修改内部list内元素
"""

