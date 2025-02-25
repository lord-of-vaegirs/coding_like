# 异步操作aiohttp 实现requests.get()同步

import asyncio
import aiohttp

urls=[
    'https://www.umei.cc/d/file/20230616/86ff25f61e20df9df6881cc1f86379a5.jpg',
    'https://www.umei.cc/d/file/20230616/dd9dd814dbb1098f4005a9d2b6ddff7d.jpg',
    'https://www.umei.cc/d/file/20230616/8d21a66a232b9d163a379a6a962c9d62.jpg'
]

async def aiodownload(url):
    name=url.rsplit('/',1)[1]
    # rsplit 按照/进行一次分割 从右开始分割 然后索引1位置的字符串
    async with aiohttp.ClientSession() as session: # 使用session 相当于异步里面的requests 并用with工具包装
        async with session.get(url) as resp: # get请求存入resp
            # 异步请求里面content text json变化成下面了
            # await resp.content.read() # 异步操作都得加await
            # await resp.text()
            # await resp.json()
            with open(name,mode='wb') as f:
                f.write(await resp.content.read())


async def main():
    tasks=[asyncio.create_task(aiodownload(url)) for url in urls]
    await asyncio.wait(tasks)


if __name__=="__main__":
    asyncio.run(main())


























