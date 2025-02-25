"""
下载西游记
"""

import requests
import asyncio  # 异步IO操作
import aiohttp  # 异步网络请求操作
import aiofiles # 异步文件操作
import json

# 1.同步操作：访问书的网页 拿到所有章节的cid
# 2.异步操作：访问每个章节的网页 下载所有的文章内容

# url='https://dushu.baidu.com/api/pc/getCatalog?data={%22book_id%22:%224306063500%22}'
header={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
}

# https://dushu.baidu.com/api/pc/getChapterContent?data={%22book_id%22:%224306063500%22,%22cid%22:%224306063500|1569782244%22,%22need_bookinfo%22:1}

async def aiodownload(cid,bid,title):
    data={
        "book_id":bid,
        "cid": f'{bid}|{cid}',
        "need_bookinfo": 1
    }
    data=json.dumps(data)
    url_c=f'https://dushu.baidu.com/api/pc/getChapterContent?data={data}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url_c) as resp:
            dic2=await resp.json()
            content=dic2['data']['novel']['content']
            async with aiofiles.open(title,mode='w',encoding='utf-8') as f:
                await f.write(content)

async def getCatalog(url):
    resp=requests.get(url,headers=header)
    dic=resp.json()
    # print(resp.json())
    book_id=dic['data']['novel']['book_id']
    it_lt=dic['data']['novel']['items']
    title_lt=[i['title'] for i in it_lt]
    cid_lt=[i['cid'] for i in it_lt]
    tasks=[asyncio.create_task(aiodownload(cid_lt[i],book_id,title_lt[i])) for i in range(len(cid_lt)) ]
    await asyncio.wait(tasks)
    # print(book_id,cid_lt)


if __name__=='__main__':
    url = 'https://dushu.baidu.com/api/pc/getCatalog?data={%22book_id%22:%224306063500%22}'
    asyncio.run(getCatalog(url))





































