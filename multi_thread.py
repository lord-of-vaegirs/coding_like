"""
多进程和多线程
线程是进程的子集
多个线程构成一个进程
python里面一个进程只有一个GIL 所以多线程也只能在一段时间内运行其中一个线程 多线程无效率提升
所以，python里面多进程比多线程更有优势，利于计算密集型
线程之间资源数据共享
进程之间互相独立，无法共享
"""


import threading
import time
from threading import current_thread



# def target(second):
#     print(f'Threading {threading.current_thread().name} is running')
#     print(f'Threading {threading.current_thread().name} sleep {second}s')
#     time.sleep(second)
#     print(f'Threading {threading.current_thread().name} is ended')
#
# print(f'Threading {threading.current_thread().name} is running')
#
# # for i in [1,5]:
# #     t=threading.Thread(target=target,args=[i])
# #     t.start()
# #      t.join()
#
# t1=threading.Thread(target=target,args=[2]) # 引入子线程1
# t1.start()
# t2=threading.Thread(target=target,args=[5]) # 引入子线程2
# t2.daemon=True # 将thread-2设置为守护线程，主线程结束时，无论其是否运行结束，都要退出
# t2.start()
#
#
# print(f'Threading {threading.current_thread().name} is ended')



# count=0
#
# class MyThread(threading.Thread):
#     def __init__(self):
#         threading.Thread.__init__(self)
#
#     def run(self):
#         global count
#         lock.acquire() # 线程上锁，别的线程只能等待
#         temp=count+1
#         time.sleep(0.001)
#         count=temp
#         lock.release() # 线程开锁
#
#
# lock=threading.Lock()
# threads=[]
# for i in range(1000):
#     thread=MyThread()
#     thread.start()
#     threads.append(thread)
# for thread in threads:
#     thread.join()
# print(f'Final count:{count}')
# # 这里最后count不是我们期待的1000，而是34，每次还不一样，说明多线程并行，有很多+1操作未生效
#
# # python里面有GIL，导致多线程运行时只能有1个线程拿到它，无法发挥多核优势

import multiprocessing

# def process(index):
#     time.sleep(index)
#     print(f'Process:{index}')
#
# if __name__=='__main__':
#     for i in range(5):
#         p=multiprocessing.Process(target=process,args=(i,))
#         p.start()
#     print(f'CPU number:{multiprocessing.cpu_count()}') # 获取运行的核数
#     for p in multiprocessing.active_children(): # 获取当前正在运行的进程名称和进程号
#         print(f'Child process name:{p.name} id: {p.pid}')
#     print('Process Ended')

# import time
# from multiprocessing import Process, Lock  # 添加缺少的time模块导入
#
#
# class MyProcess(Process):
#     def __init__(self, loop, lock):
#         super().__init__()  # 使用super()规范继承
#         self.loop = loop
#         self.lock = lock
#
#     def run(self):
#         for count in range(self.loop):
#             time.sleep(0.1)
#             with self.lock:  # 使用上下文管理器自动处理锁的获取/释放
#                 print(f'Pid: {self.pid} LoopCount: {count}')
#
#
# if __name__ == '__main__':
#     lock = Lock()  # 必须实例化Lock对象（添加括号）
#     processes = []
#
#     for i in range(10, 15):
#         p = MyProcess(i, lock)
#         processes.append(p)
#         p.start()
#
#     for p in processes:
#         p.join()  # 添加进程等待，确保主进程等待子进程结束

    # for i in range(2,5):
    #     p=MyProcess(i)
    #     p.daemon=True
    #     p.start()
    #     p.join(2)

    #print('Main Process ended')

# 进程里面同样有守护进程 父进程结束，子进程自动终止 daemon
# 进程等待 join方法 加入的进程全运行完毕后才会结束
# 可以加入主进程最长等待时间 防止超时等待 join(second)
# terminate方法终止某个子进程
# is_alive方法判断进程是否还在运行

# def process():
#     print('Starting')
#     time.sleep(5)
#     print('Finished')
# if __name__=='__main__':
#     p=Process(target=process)
#     print('Before: ',p,p.is_alive())
#     p.start()
#     print('During: ',p,p.is_alive())
#     p.terminate()
#     print('Terminate: ',p,p.is_alive())
#     p.join()
#     print("Join: ",p,p.is_alive())

# terminate之后记得join更新状态

# 进程互斥锁 保证多个进程运行期间任意时间只能一个进程输出 其他等待

# 信号量来控制并发进程数，做到控制同一时间多进程共享资源

# from multiprocessing import Process, Semaphore, Lock, Queue, Value
# import time
#
#
# class Consumer(Process):
#     def __init__(self, buffer, empty, full, lock):
#         super().__init__()
#         self.buffer = buffer
#         self.empty = empty
#         self.full = full
#         self.lock = lock
#
#     def run(self):
#         while True:
#             self.full.acquire()  # 等待有产品可消费
#             with self.lock:  # 对缓冲区的操作加锁
#                 self.buffer.get()
#                 print(f'Consumer {self.pid} pop an element')
#                 time.sleep(0.1)
#             self.empty.release()  # 释放空位
#
#
# class Producer(Process):
#     def __init__(self, buffer, empty, full, lock):
#         super().__init__()
#         self.buffer = buffer
#         self.empty = empty
#         self.full = full
#         self.lock = lock
#
#     def run(self):
#         while True:
#             self.empty.acquire()  # 等待有空位可生产
#             with self.lock:  # 对缓冲区的操作加锁
#                 self.buffer.put(1)
#                 print(f'Producer {self.pid} append an element')
#                 time.sleep(0.1)
#             self.full.release()  # 增加可用产品数
#
#
# if __name__ == '__main__':
#     # 共享资源初始化（必须通过参数传递）
#     buffer = Queue(10)
#     empty = Semaphore(10)  # 初始空位数量=缓冲区容量
#     full = Semaphore(0)  # 初始产品数量=0
#     lock = Lock()
#
#     # 创建进程时传递共享对象
#     producers = [Producer(buffer, empty, full, lock) for _ in range(2)]
#     consumers = [Consumer(buffer, empty, full, lock) for _ in range(3)]
#
#     # 设置守护进程 + 超时控制
#     for p in producers + consumers:
#         p.daemon = True
#         p.start()
#
#     try:
#         while True:  # 主线程保持运行
#             time.sleep(1)
#     except KeyboardInterrupt:
#         print("\nMain process ending...")

# Queue 队列 让进程共享数据
# 管道 两个进程之间通信的通道
# 单向 half-duplex 一个进程发消息 另一个进程收消息
# 双向 deplex 互相收发


# pool 进程池
# from multiprocessing import Pool
# import time
#
# def function(index):
#     print(f'Start process: {index}')
#     time.sleep(3)
#     print(f'End process: {index}')
#
# if __name__=='__main__':
#     pool=Pool(processes=3) # 规定进程池大小 一次可容纳3个进程 最多不超过系统cpu数
#     for i in range(1000):
#         pool.apply_async(function,args=(i,)) # 加入进程
#
#     print('Main Process started')
#     pool.close()
#     pool.join()
#     print('Main Process ended')
#


from multiprocessing import Pool
import urllib.request
import urllib.error
import socket
import ssl

def scrape(url):
    try:
        urllib.request.urlopen(url)
        print(f'URL {url} Scraped')
    except (urllib.error.HTTPError,urllib.error.URLError, socket.error, ssl.SSLError, ConnectionResetError, TimeoutError):
        print(f'URL {url} not Scraped')

if __name__=='__main__':
    pool=Pool(processes=3)
    urls=[
        'https://www.baidu.com',
        'http://www.meituan.com/',
        'http://blog.csdn.net/',
        'https://xxxyxxx.com/'
    ]
    pool.map(scrape,urls) # scrape位置放置进程执行方法，urls位置放置可迭代容器（如列表）
    pool.close()


