from scipy.stats import randint


class Student:
    name=None
    age=None
    height=None
    nationality=None

class teacher:
    name=None
    age=None
    subject=None
    class_in_charge=None

class staff:
    name=None
    age=None
    post=None



stu_1=Student()
stu_2=Student()

stu_1.name='张三'
stu_1.age=19
stu_1.height=165
stu_1.nationality='中国'

stu_2.name='李四'
stu_2.age=18
stu_2.height=174
stu_2.nationality='俄罗斯'

# print(stu_1)
# print(stu_2)

tch_1=teacher() # class() ()里面传的是self的参
tch_2=teacher()
tch_3=teacher()

tch_1.name='GB'
tch_2.name='XBB'
tch_3.name='LL'
tch_1.age=35
tch_2.age=39
tch_3.age=randint(20,45,1)
tch_1.subject='math'
tch_2.subject='physics'
tch_3.subject='???'
tch_1.class_in_charge=[9,13]
tch_2.class_in_charge=[11,13]
tch_3.class_in_charge=[7,11]

stf_1=staff()
stf_2=staff()

stf_1.name='ZJC'
stf_1.age=randint(50,65,1)
stf_1.post='Chairman'

stf_2.name='ZLJ'
stf_2.age=randint(50,60,1)
stf_2.post='headmaster'


class School:
    stud=None
    teacher=None
    staff=None
    def go_to_school(self): # self相当于c++里面的this指针
        print('I have gone to school! ')
    def leave_school(self):
        print('I have to go home!')
    def happy_new_year(self):
        print('祝八中学子2025新年快乐！')
    def say_hi(self,num,typ):
        if typ==1:
            print(f'hello! I\'m {self.stud[num].name}')
        elif typ==2:
            print(f'hello! I\'m {self.teacher[num].name}')
        else:
            print(f'hello! I\'m {self.staff[num].name}')

school_8=School()
school_8.stud=[]
school_8.stud.append(stu_1)
school_8.stud.append(stu_2)
school_8.teacher=[]
school_8.teacher.append(tch_1)
school_8.teacher.append(tch_2)
school_8.teacher.append(tch_3)
school_8.staff=[]
school_8.staff.append(stf_1)
school_8.staff.append(stf_2)


school_8.say_hi(num=0,typ=1)
school_8.go_to_school()
school_8.leave_school()
school_8.happy_new_year()
print('--------------------------------')
school_8.say_hi(num=1,typ=1)
school_8.go_to_school()
school_8.leave_school()
school_8.happy_new_year()
print('--------------------------------')
school_8.say_hi(num=0,typ=2)
school_8.go_to_school()
school_8.leave_school()
school_8.happy_new_year()
print('--------------------------------')
school_8.say_hi(num=1,typ=2)
school_8.go_to_school()
school_8.leave_school()
school_8.happy_new_year()
print('--------------------------------')
school_8.say_hi(num=2,typ=2)
school_8.go_to_school()
school_8.leave_school()
school_8.happy_new_year()
print('--------------------------------')
school_8.say_hi(num=0,typ=3)
school_8.go_to_school()
school_8.leave_school()
school_8.happy_new_year()
print('--------------------------------')
school_8.say_hi(num=1,typ=3)
school_8.go_to_school()
school_8.leave_school()
school_8.happy_new_year()




class clock:


    def __init__(self,id,price): # 构造魔术方法
        self.id=id
        self.price=price

    def __str__(self): # str魔术方法 把object转换成str
        return f'id: {self.id}, price: {self.price}'

    def __lt__(self,other): # lt魔术方法 小于号的重载； other是另一个传入的对象
        return self.price<other.price

    def __le__(self,other): # le魔术方法 小于等于号的重载
        return self.price<=other.price

    def __eq__(self,other):
        return self.price==other.price

    def ring(self):
        print('ring!!!')


clock1=clock('001',19.99)
clock2=clock('002',9.99)
clock3=clock('003',99.99)

for i in (clock1,clock2,clock3):
    # print(f'id: {i.id}, price: {i.price}')
    print(i)
    i.ring()
print(clock1<clock2)
print(clock1<clock3)
print(clock2<clock3)
print(clock1<=clock2)
print(clock1<=clock3)
print(clock2<=clock3)
print(clock1==clock2)
print(clock1==clock3)
print(clock2==clock3)

# __init__初始化 构造函数 就可以在创建对象的（）中传参即可
# __init__里面即可填入类的属性，不必在外单独定义
















