f=open("bill.txt","r")
f2=open("bill.txt.bak","a",encoding="UTF-8")
for line in f:
    str=f.readline()
    lt=str.split(',')
    if lt[-1]=="测试" :
        continue
    else:
        f2.write(str)
f2.close()
f.close()




