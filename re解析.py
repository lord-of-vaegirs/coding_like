"""
re regular expression
正则表达式
字符串进行匹配
速度快 效率高 准确性高 难度也大

正则的语法：使用元字符进行排列组合来匹配字符串
在线测试正则表达式：https://tool.oschina.net/regex/
元字符：具有固定含义的特殊符号

. 匹配除了换行符以外的任意字符 一个点对应每行一个字符 两个点对应每行两个字符
\w 匹配字母或数字或下划线
\s 匹配任意空白符
\d 匹配数字
\n 匹配一个换行符
\t 匹配一个制表符

^ 匹配字符串的开始（准确说是标定开始的格式） 如：^/d 开始就得是一个数字
$ 匹配字符串的结尾

\W 匹配非字母或数字或下划线
\D 匹配非数字
\S 匹配非空白符
a|b 匹配字符a或b
() 匹配括号内的表达式，也表示一个组
[...] 匹配字符组中的字符 出现了组中字符，就输出 如[0-9A-Za-z]
[^...] 匹配除了字符组中字符的所有字符

量词：控制前面元字符出现次数
* 重复零次或者更多次
+ 重复一次或更多次
？ 重复零次或一次
{n} 重复n次
{n,} 重复n次或更多次
{n,m} 重复n到m次

贪婪匹配和惰性匹配
.* 一直匹配到最远的一次结果 贪婪匹配
.*? 只匹配到最近一次的结果 惰性匹配
obj1.*?obj2 从obj1开始匹配，到第一个obj2结束
.*?obj 每一次匹配都是从任意字符到obj
"""
import re

lt=re.findall("\\d+",'我的电话号是:10086,我女朋友电话是10085')
# findall(pattern,string) 匹配字符串中所有符合正则的内容 返回一个列表
print(lt)

# finditer 匹配字符串中所有的内容[返回的是迭代器] 想要拿到结果，得要用group方法
it= re.finditer("\\d+",'我的电话号是:10086,我女朋友电话是10085')
for i in it :
    print(i.group())

# search返回的结果是match对象，拿数据需要group方法，找到一个结果就返回
s=re.search("\\d+",'我的电话号是:10086,我女朋友电话是10085')
print(s.group())

# match从头开始匹配 第一个字符如果就错了的话判定全错 也是得用group方法取到
s=re.match('\\d+','10086,我女朋友电话是10085')
print(s.group())

# 预加载正则表达式
obj=re.compile('\\d+')
res=obj.finditer('我的电话号是:10086,我女朋友电话是10085')
for i in res:
    print(i.group())

s="""
<div class='joy'><span id='1'>郭麒麟</span></div>
<div class='jj'><span id='2'>宋轶</span></div>
<div class='jolin'><span id='3'>大聪明</span></div>
<div class='sylar'><span id='4'>范思哲</span></div>
<div class='tory'><span id='5'>胡诹</span></div>
"""

obj=re.compile("<div class='(?P<class>.*?)'><span id='(?P<id>.*?)'>(?P<gigity>.*?)</span></div>",re.S) # re.S 隶属于flags参数 让.能匹配换行符
# 利用正则表达式的地方，两边加上圆括号，里面前置?P<组名> 就可以在后面的group方法里面通过组名调到对应的数据了

res2=obj.finditer(s)
for i in res2:
    # print(i.group(1),end=' ')
    # print(i.group(2),end=' ')
    # print(i.group(3))
    print(i.group('class'),end=' ')
    print(i.group('id'),end=' ')
    print(i.group('gigity'))





