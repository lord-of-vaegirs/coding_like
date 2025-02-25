# bool有True False
# 比较运算符同c
print("%s" % (10<5))
b1=True
b2=False
# if语句 结构为 ‘if 判断语句 ：’
# if满足之后执行的语句必须有缩进表示归属
if (10<5)==b1 :
    print("correct")
else :
    print("incorrect")
# else为if不满足的情况执行的语句
name="lamba"
mns="234"
tno=12
kr=13
kx=23
# elif 等同于 c里面的else if（）
if tno+kr<kx :
    print("correct")
elif tno+kx<kr :
    print("coxxect")
else :
    print("incorrect")
# 嵌套if
if tno<kr :
    if tno+kr<25:
        print("do")
    else :
        print("undo")
else :
    print("undo")




