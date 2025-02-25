"""
容器的通用操作
len()
统计长度
max()
找到最大元素
min()
找到最小元素

list()
tuple()
str()
set()
将容器之间互相转换

排序
sorted(容器，[reverse=True])
后面的参数控制排序规则
True是反向 从大到小
False是正向 从小到大 也是系统默认的
"""
lt1=[1,2,3,4,5]
tp1=(1,2,3,4,5)
str1="abcdefg"
set1={1,2,3,4,5}
dict1={'k1':1,'k2':2,'k3':3,'k4':4,'k5':5}

print(len(lt1))
print(len(tp1))
print(len(str1))
print(len(set1))
print(len(dict1))

print(max(lt1))
print(max(tp1))
print(max(str1))
print(max(set1))
print(max(dict1))
# dict的max比的是key
print(min(lt1))
print(min(tp1))
print(min(str1))
print(min(set1))
print(min(dict1))

print(f"{list(lt1)}")
print(f"{list(tp1)}")
print(f"{list(str1)}")
print(f"{list(set1)}")
print(f"{list(dict1)}")
# list可以全部转换 dict转list只保留key
print(f"{tuple(lt1)}")
print(f"{tuple(tp1)}")
print(f"{tuple(str1)}")
print(f"{tuple(set1)}")
print(f"{tuple(dict1)}")
# tuple可以全部转换 dict转tuple只保留key
print(f"{str(lt1)}")
print(f"{str(tp1)}")
print(f"{str(str1)}")
print(f"{str(set1)}")
print(f"{str(dict1)}")
# str全部转为“”，里面是原来各自的字面量 输出时“”被省了
print(f"{set(lt1)}")
print(f"{set(tp1)}")
print(f"{set(str1)}")
print(f"{set(set1)}")
print(f"{set(dict1)}")
# set可以全部转换 dict转set只保留key

print(f"{sorted(lt1)}")
print(f"{sorted(tp1)}")
print(f"{sorted(str1)}")
print(f"{sorted(set1)}")
print(f"{sorted(dict1)}")
# sorted()函数是将元素排序后放入list容器中的 dict排序value会丢失
print(f"{sorted(lt1,reverse=True)}")
print(f"{sorted(tp1,reverse=True)}")
print(f"{sorted(str1,reverse=True)}")
print(f"{sorted(set1,reverse=True)}")
print(f"{sorted(dict1,reverse=True)}")
# sorted()先将容器转换成list再排序



