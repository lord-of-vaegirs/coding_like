import asyncio
import time


async def download(url):
    print('开始下载')
    await asyncio.sleep(2)
    print('下载完毕')



async def main():
    urls=[
        'https://www.baidu.com',
        'https://www.bilibili.com',
        'https://www.sougou.com'
    ]

    tasks=[asyncio.create_task(download(url)) for url in urls]

    await asyncio.wait(tasks)

if __name__ == '__main__':
    t1=time.time()
    asyncio.run(main())
    t2=time.time()
    print(t2-t1)