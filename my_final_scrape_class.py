"""
流程：
1.拿到主页面源代码 找到iframe（为了找到m3u8文件）
2.从iframe页面源代码中拿到m3u8文件
3.下载第一层m3u8文件 -> 拿到第二层m3u8文件
4.下载视频
5.下载密钥，进行解密（如果m3u8文件里面没有加密，跳过此步）
6.合并所有ts文件

mac合并ts文件 ：import os
cat 1.ts 2.ts 3.ts > xxx.mp4
s=" ".join(lst) # 把所有ts文件名中间用空格空开并制成字符串
os.system(f"cat {s} > movie.mp4")
"""
import re
import requests
import aiohttp
import aiofiles
import asyncio

header={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
}


def get_first_m3u8(url):

    obj = re.compile(r'<div class="stui-player__video clearfix">.*?<script type="text/javascript">.*?"vod_class":".*?"},"url":"(?P<url2>.*?)"',re.S)

    resp = requests.get(url,headers=header)
    # print(resp.text)

    return obj.search(resp.text).group('url2')

def download_m3u8_file(url,name):
    resp=requests.get(url,headers=header)
    with open(name,mode='wb') as f:
        f.write(resp.content)

async def download_ts(url,name,session):
    async with session.get(url,headers=header) as resp:
        content=resp.content.read()
        async with aiofiles.open(f"video2/{name}",mode='wb') as f:
            await f.write(content)
            print(f'{name}完成了')

async def aio_download():
    tasks=[]
    async with aiohttp.ClientSession() as session:
        async with aiofiles.open('纸牌屋第一季第一集_second.m3u8', mode='r', encoding='utf-8') as f:
            async for line in f:
                if str(line).startswith('#'):
                    continue
                line = str(line).strip()
                ts_url = line
                task = asyncio.create_task(download_ts(ts_url, line.split('/')[-1].replace('jpeg','ts'),session))
                tasks.append(task)
            await asyncio.wait(tasks)
            print('全部完成了')


def main(url):
    url2 = get_first_m3u8(url)

    url2=url2.replace('\\','')

    # print(url2)

    download_m3u8_file(url2,'纸牌屋第一季第一集_first.m3u8')

    with open('纸牌屋第一季第一集_first.m3u8',mode='r',encoding='utf-8') as f:
        for line in f:
            if line.startswith('#'):
                continue
            line=line.strip()
            str3=str(line)
            url3=url2.split('index')[0]+str3
            download_m3u8_file(url3,'纸牌屋第一季第一集_second.m3u8')

    asyncio.run(aio_download())



if __name__=='__main__':
    url='https://www.qdlsly.com/play-18988-1-1.html'
    main(url)


# 简单的问题复杂化
# 复杂的问题简单化




