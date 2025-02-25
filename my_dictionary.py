"""
dictionary
key:value
一个关键值对应一个信息
可以通过key来寻找value
{key1:value1,key2:value2,...}
my_dict={key1:value1,key2:value2,...}
my_dict=dict()
my_dict={} 这两种都可以定义空字典
不允许重复
不可以使用下标索引
只能用key来索引
"""
my_dict={"python":1,"cpp":2,"java":3}
print(type(my_dict))
print(my_dict)
x=my_dict["python"]
print(x)
"""
字典可以嵌套
key和value可以是不同类型
但key不能是dict
value可以是dict，实现嵌套
"""
dict1={1:"python",2:'cpp'}
dict2={1:'apple',2:'microsoft'}
dict3={1:'phone',2:'pc'}
dic={1:dict1,2:dict2,3:dict3}
print(dic)
print(dic[3][1])

"""
功能：
1.新增 
dict[key]=value 
原字典被修改，增加了新元素
2.更新
dict[key]=value
原字典被修改，元素被更新
这是对老的key更新
3.删除
dict.pop(key)
获取key对应的value，同时从字典里删除key对应的数据
4.清空
dict.clear()
5.获取全部的key(用一个变量去接收）
dict.keys()
6.遍历
利用keys来遍历 for循环
7.统计元素数量 len
"""
dict1[3]='java'
print(dict1)
dict1[1]='python3'
print(dict1)
x=dict1.pop(2)
print(x)
print(dict1)
dict1.clear()
print(dict1)
k=dict2.keys()
print(k)

for i in k:
    print(i) # 输出key
    print(dict2[i]) # 输出对应的value

print(len(dic))

"""
dictionary 特点
可以容纳多个元素 
可以容纳不同类型的元素
不允许重复key存在
每一个key对应一个value
不支持下标索引
可以修改元素
只支持for循环
"""