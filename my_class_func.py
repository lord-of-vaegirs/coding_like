"""
以两个下划线开头的变量为私有成员
"""
import json


class Phone:
    IMEI=None
    producer='APPLE'
    __current_voltage=1.2
    def __keep_single_core(self):
        print('让cpu单核运行')

    def call_by_5g(self):
        if self.__current_voltage>=1:
            print('5g通话已开启')
        else:
            self.__keep_single_core()
            print('电量不足，无法使用5g通话，并已设置为单核运行进行省电')

class NFC:
    nfc_type='第五代'
    producer='APPLE'

    def read_card(self):
        print('NFC读卡')

    def write_card(self):
        print('NFC写卡')

class RemoteControl:
    rc_type='001'
    def control(self):
        print('远程控制')

phone1=Phone()
phone1.call_by_5g()

"""
继承
单继承：class name(father_name):
            ...
多继承：class name(fname1,fname2,fname3,...):
            ...
"""
class Phone2024(Phone):
    face_id='00001'

    def call_by_6g(self):
        print('6g通话新功能')


phone2=Phone2024()
print(phone2.producer)
phone2.call_by_5g()
phone2.call_by_6g()


class Phone20xx(Phone,NFC,RemoteControl):
    pass # 如果新的类只是想单纯的继承多个父类的功能，直接pass就好了

phone3=Phone20xx()
print(phone3.producer)
phone3.read_card()
phone3.write_card()
phone3.control()

# 多继承 如果遇到不同父类里面的同名属性，以左侧继承为优先，谁先传入，谁被赋值

# 复写 在子类里面定义与父类同名变量，并为其赋予新的值
class father:
    age=48
    id='001'

class son(father):
    age=20

son1=son()
print(son1.age)
print(son1.id)

# 在子类里面调用父类同名成员有两种方法

class grandson(son):
    age=1
    id='002'
    def call_father_age(self):
        print(f'father\'s age is {son.age}') # 用父类的class名来调用父类同名成员
        print(super().age) # super().父类成员也可以用于调用父类同名成员

grandson1=grandson()
print(grandson1.age)
grandson1.call_father_age()

"""
类型注解
变量：类型=。。。
标明该变量是什么类型或者什么容器
容器的类型注解还可以在类型名后面加上中括号，里面填上容器内容的类型
元组类型设置类型详细注解，需要将每个元素都标记出来
字典类型设置类型详细注解，需要2个类型，第一个是key，第二个是value

还有第二种方式进行注解
在变量的定义后面加上注释 type:类型 即可

只是一种提示，并非真正的确定了类型

函数方法的类型注解：
def fucn(v1:type1,v2:type2,...):
    ...
这样定义函数即可给形参注解

def func(v1:type1,v2:type2,...) -> type_return :
    ...
这样即可标明返回值的类型

容器的类型注解，还可以借助union来标注
exp:
from typing import Union
my_list:list[Union[str,int]]=[1,2,'string'.'beancurd']
my_dict:dict[str,Union[str,int]]={'name':'Jack','age':31}
同样，Union还可以用在func里面形参和返回值的类型注解上

"""
my_list:list=[1,2,3]
a:int = 12
my_tuple:tuple[str,int,bool]=('string',12,True)
my_set:set[int]={1,2,4}
my_dict:dict[str,int]={'string':888}

var1=12 # type: int

import json

var2 = json.loads('{"name":"zhangsan"}')  # 正确格式
print(var2)  # 输出: {'name': 'zhangsan'}
"""
多态
同样的行为，传入不同的对象，得到不同的状态

抽象方法：方法体是空实现的（pass）称为抽象方法
抽象类：含有抽象方法的类
父类来决定有哪些方法
具体的实现，由子类自行决定
"""
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        print('woof!!!')

class Cat(Animal):
    def speak(self):
        print('miaowoo!')

def make_noise(animal:Animal): # 本来应该传入父类对象
    animal.speak()

dog=Dog()
cat=Cat()

make_noise(dog) # 下面实际传入的是子类对象
make_noise(cat)


class AC:
    def cool_wind(self):
        pass
    def hot_wind(self):
        pass
    def swing_1_r(self):
        pass

class Geli(AC):
    def cool_wind(self):
        print('格力的冷风')
    def hot_wind(self):
        print('格力的热风')
    def swing_1_r(self):
        print('格力的摆风')

class Meidi(AC):
    def cool_wind(self):
        print('美的的冷风')
    def hot_wind(self):
        print('美的的热风')
    def swing_1_r(self):
        print('美的的摆风')

def make_cool(ac:AC):
    ac.cool_wind()

def make_hot(ac:AC):
    ac.hot_wind()

def make_swing(ac:AC):
    ac.swing_1_r()

m=Meidi()
g=Geli()

make_cool(m)
make_hot(m)
make_swing(m)

make_cool(g)
make_hot(g)
make_swing(g)






