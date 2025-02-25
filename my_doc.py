"""
文件

编码
表示二进制与内容之间转换的逻辑
常用UTF-8编码

对文件的操作
1.打开 open(name,mode,encoding)
name是目标文件名，可以是具体路径
mode设置打开方式(只读r、写入w、追加a)
encoding编码方式（UTF-8)

2.读取 read
doc.read(num)
num表示读取数据的长度（字节数），如果没填num，那就读取所有数据
readlines()方法 可以按照行的方式吧整个文件的内容一次性读取，
返回一个列表，每一行的数据为一个元素
readline() 一次读一行内容
for循环读取文件行
for line in open(name,mode):
    print(line)
3.关闭
f.close()
4.with open语法
with open(name,mode) as f:
    f.readline()
在执行完内部语句块后自动关闭文件

5.写入
5.1 write 写入 并未真正写入，而是积攒在缓冲区中
f.write(“”)
5.2 flush 刷新 内容真正写入文件
f.flush()
用写入模式打开文件，如果文件不存在，直接徽新建一个对应的文件

6.追加
只需把打开方式换成“a"
其他操作同写入
文件不存在就创建文件，存在就追加
"""

f=open("/Users/lxjarctane2/Documents/pythonide/test01.txt","r",encoding="UTF-8")
# print(f"{f.read(10)}")
# print(f"{f.read()}")
# 每一次read都从上次读取结束的位置继续读取
# print(f"{f.readlines()}")
# 这里就读不到了 除非之前没读取
# print(f"{f.readline()}")
# print(f"{f.readline()}")
# print(f"{f.readline()}")
# print(f"{f.readline()}")
# print(f"{f.readline()}")

for i in f:
    print(i)
# 每次循环记录了每一行的内容
f.close()
# 解除对文件的占用

# time.sleep(time)可以使程序在该行暂停time秒
with open("/Users/lxjarctane2/Documents/pythonide/test01.txt","r") as f:
    for i in f:
        print(f"{f.readline()}")

f=open("/Users/lxjarctane2/Documents/pythonide/test02.txt","w",encoding="UTF-8")
# 不存在的文件直接新建 存在的文件再次写入会把之前的内容全部清空
f.write("hello world!")
# 写入缓冲区
f.flush()
# 从缓冲区录入内存
f.close()
# close内置flush功能，可以不需要flush了这里
f=open("/Users/lxjarctane2/Documents/pythonide/test02.txt","w",encoding="UTF-8")
f.write("123")
f.close()

f=open("/Users/lxjarctane2/Documents/pythonide/test02.txt","a",encoding="UTF-8")
f.write("python")
f.flush()
f.close()



