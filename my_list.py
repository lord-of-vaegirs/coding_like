# list链表
# [ele1,ele2,ele3,...]
# list定义方式 每个元素之间用逗号隔开
# var=[]
# var=list()
var1=list()
var2=["python",12,34.5]
# list里面元素类型不受限制，不用同类型
print(var2)
print(type(var2))
# list支持嵌套
var3=[var2,10,29]
print(var3)
# list 的下标索引
# 跟传统语言一样 从0开始
# _list[x] 求第x-1个元素
print(var3[0])
# 想取嵌套list里面的元素，就用多层[]即可
print(var3[0][0])
# 下标索引别超范围否则报错！
# list下标索引支持反向索引 从最后一个元素开始 为-1依次往下递减
print(var3[-1])
"""
list的操作方法
函数就是方法
只是方法是写在class里的
"""
"""
1.查询方法
查找指定元素的下标
找不到报错valueerror
列表.index(元素)
"""
mylist=[12,34,56,90,"nihao","hello","bonjour","ohiyo","hallo","ciallo"]
x=mylist.index("nihao")
print(x)

"""
2.修改
列表[]=值
"""
mylist[1]=20
mylist[-1]="cpp"
print(mylist)

"""
3.insert
list.insert(index,ele)
index用正反向都行，但是插入之后，所有index及之后位置的原本元素向后移一位
"""
mylist.insert(0,"pp")
print(mylist.index("pp"))
mylist.insert(-2,"new")
print(mylist)

"""
4.append
list.append(ele)
将ele追加至list尾部
如果想要追加list到尾部，要用extend（）
"""
mylist.append(100)
print(mylist)
mylist.extend(var2)
print(mylist)
# 查询只能查找目标在list中第一次出现的位置
print(mylist.index(12))

"""
5.delete
5.1 del list[index]
5.2 list.pop(index)
还可以用变量接收pop出的元素
"""
del mylist[1]
z=mylist.pop(-1)
print(mylist)
print(z)

"""
6.remove
移除某个元素在list中从前往后第一次出现的匹配项
list.remove(ele)
"""
p=mylist.remove("hallo")
print(mylist)
if not p:
    print("none")
else:
    print("yes")

"""
7.clear
清空整个list
list.clear()

8.count
统计某个元素在list中的数量
list.count(ele)
然后可以用变量来接收结果
"""
num=mylist.count(12)
print(num)
mylist.clear()
print(mylist)

"""
9.统计列表的长度 len
len(list)
可以用变量来接收
"""
len2=len(var2)
print(len2)

"""
list 特点
可以容纳多个元素 上限为2^63-1
可以容纳不同类型的元素
数据有序储存
允许重复元素存在
可以修改元素
"""

"""
list 的迭代/遍历
while循环
for循环
"""
def list_while(ml):
    ind=0
    while ind<len(ml):
        print(ml[ind])
        ind+=1
# while需要自己写迭代语句
def list_for(ml):
    for i in range(len(ml)):
        print(ml[i])
# for自己就会++
ml=["python",'cpp','c','c#','java','pascal','go','html']
list_while(ml)
list_for(ml)





