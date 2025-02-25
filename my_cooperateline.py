# sleep时 系统处于阻塞状态
# IO时，系统处于阻塞状态
# 对网站发送请求得到返回之前，也处于阻塞状态

# 协程就是 当程序遇见IO操作的时候，可以选择性的切换到其他任务上
# 多任务异步操作

import asyncio
import time


async def func1():
    print('你好啊111')
    await asyncio.sleep(3)
    print('你好啊111')

async def func2():
    print('你好222')
    await asyncio.sleep(2)
    print('你好222')

async def func3():
    print('你好333')
    await asyncio.sleep(4)
    print('你好333')


async def main():
    tasks=[
        asyncio.create_task(func1()),
        asyncio.create_task(func2()),
        asyncio.create_task(func3())
    ] # 得启用异步创建任务迭代对象
    await asyncio.wait(tasks) # await 一般放在协程对象前面

    """
    第一种写法：
    f1=func1()
    await asyncio.create_task(f1) 
    第二种写法：推荐
    tasks=[
        asyncio.create_task(func1()),
        asyncio.create_task(func2()),
        asyncio.create_task(func3())
    ]
    asyncio.wait(tasks)
    
    
    """



if __name__=="__main__" :
    # f1=func1() # 异步协程函数 产生一个对象
    # f2=func2()
    # f3=func3()
    # asyncio.run(f1) # 运行协程 需要asyncio模块
    # asyncio.run(f2)
    # asyncio.run(f3)


    t1=time.time()

    # 一次性启动多个任务
    asyncio.run(main()) # 走异步主函数


    t2=time.time()
    print(t2-t1)


















