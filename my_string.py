"""
字符串
正反向索引都支持
只读 不可写
"""
mystr="hello"

"""
功能：
索引 string.index(ele)
替换 string.replace(str1,str2) 必须用新的字符串去接收才行
分割 string.split(分割符字符串）字符串本身不变，只是划分成多个字符串，存入一个列表对象 分割符字符串得在string里面，且分割后list里面没有它
规整 string.strip(string2)或string.strip() 前者前后按字符去除 后者去除前后空格
统计 string.count(string2) string2出现次数
取长度 len(string)
追加 直接str=str+"xxx"即可
遍历
"""

x=mystr.index("ell")
print(x)
str2=mystr.replace('h','op')
print(str2)
mystr="opm sha bi ni tian wow"
list1=mystr.split(' ')
print(list1)
str3="qwertyuiop"
list2=str3.split('t')
print(list2)

str4=" itmanip "
str5=str4.strip()
print(str5)
str6=str4.strip(" ip")# 即使传入字符串 他还是按字符去的
print(str6)

y=str4.count('i')
print(y)

print(len(str4))

id=0
while id<len(str4):
    print(f"{str4[id]}",end=' ')
    id+=1
print()
# 序列的切片 从序列里面取出子序列
# 序列[起始下标：结束下标：步长]
# 起始下标可以为空，表示从头开始
# 结束下标可以为空，表示到尾结束；不包括本身位置！
# 步长可以为负，表示反向，起始下标和结束下标也要用相应的负值下标索引表示
# 切片不会影响序列本身
mylist=[0,1,2,3,4,5,6]
print(mylist[0::])
tuple=(2,3,1,4,7,5,6)
print(tuple[1::2])
string1="hello"
string3=string1[-1:-6:-1]
print(string3)


