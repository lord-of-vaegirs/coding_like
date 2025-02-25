# 多线程
from threading import Thread

def func():
    for i in range(1000):
        print("func:",i)

# Thread 继承类
class MyThread(Thread):
    def run(self):
        for i in range(1000):
            print("子线程",i)


if __name__=='__main__':
    t=Thread(target=func,args=("周杰伦",)) # 创建一个子线程 目标是进行func函数
    t.start() # 告知线程可以开始工作了，但是具体什么时候开始，得由CPU决定
    t3=Thread(target=func,args=("王力宏",)) # args=(,) args传入参数，且必须是元组
    t3.start()
    t2=MyThread() # 创建thread继承类的对象 传入参数可以自己写__init__构造函数
    t2.start() # 一定记住要用start 来启动线程 run会自动执行
    for i in range(1000):
        print("main:",i)

    # 还可以使用继承类






















