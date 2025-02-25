"""
set
不重复元素
语法： {ele,ele2,ele3,...}
_set={ele1,ele2,...}
_set=set() 定义空集合的唯一方式
乱序组合
不支持下标索引
集合不是序列
可修改
"""
set1={12,34,"lining",12}
print(set1)

"""
功能
1.add
set.add(ele)
2.remove
set.remove(ele)
3.pop 随机取出一个元素
set.pop()
4.clear
set.clear()
5.difference 取差集
set1.difference(set2)
set1-set2的意思 得到一个新集合，原集合不变
6.difference_update 消除差集
set1.difference_update(set2)
set1里面与set2相同的元素被消除
7.union 合并
set1.union(set2)
组成新集合，原集合不变
8.len 统计长度
set.len()
9.遍历
只能用for循环
"""
set1.add("python")
print(set1)
set1.remove(12)
print(set1)
x=set1.pop()
print(x)
print(set1)
set1.clear()
print(set1)
set1={100,89,"iron","germany reich"}
set2={89,100}
set3=set1.difference(set2)
print(set3)
set1.difference_update(set2)
print(set1)
set1={10,20,30}
set2={40,60,90}
set3=set1.union(set2)
print(set3)
print(len(set3))

for i in set3:
    print(f"集合元素：{i}")

"""
set 特点
可以容纳多个元素 
可以容纳不同类型的元素
数据无序储存
不允许重复元素存在
可以修改元素
只支持for循环
"""
