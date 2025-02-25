# //*[@id="line-list"]/li[2]/a

"""
https://php.playerla.com/mjdplay/super.php?id=CNzI5XzBqdWhl&next=https://www.mjtt5.net/dy/siwangshishe/0-1.html


"""
import re
import requests
import asyncio
import aiohttp
import aiofiles
import os

header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
    }
url = 'https://php.playerla.com/mjdplay/super.php?id=CNzI5XzBqdWhl&next=https://www.mjtt5.net/dy/siwangshishe/0-1.html'

# params={
#     "id": "CNzI5XzBqdWhl",
#     "next": "https://www.mjtt5.net/dy/siwangshishe/0-1.html"
# }

async def download_ts(url,name,session):
    async with aiofiles.open(f'deadpoem_doc/{name}', mode='wb') as f:
        async with session.get(url, headers=header) as resp:
            await f.write(await resp.content.read())
    print('over!')



async def aio_download():
    tasks=[]
    async with aiohttp.ClientSession() as session:
        with open('deadpoem.m3u8', mode='r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('#'):
                    continue
                else:
                    line = line.strip()
                    ts_url = line
                    task = asyncio.create_task(download_ts(ts_url,ts_url.split('/')[-1],session))
                    tasks.append(task)
            await asyncio.gather(*tasks)
            print('全部下载完成了！！！')


def main():
    # obj=re.compile(r'quality: .*?"url":"(?P<m3u8>.*?)"',re.S)
    # resp = requests.get(url, headers=header,params=params)
    # # print(resp.text)
    # m3u8_url=obj.search(resp.text).group('m3u8').replace('\\','')
    # print(m3u8_url)
    # 本来应该要拼接的，但是时间问题没做，直接用现成的了
    m3u8_url='https://six.svipplay.com/lzm3u8/6f80f9b64d1abd1aa80852577305cc26.m3u8?token=CswMeJ337ZQXusqE5Yfd6Q&expires=1739545423'
    resp2=requests.get(m3u8_url,headers=header)
    with open('deadpoem.m3u8',mode='wb') as f:
        f.write(resp2.content)
    print('over!')
    asyncio.run(aio_download())



if __name__=='__main__':
    main()




# https://vip.lzcdn2.com/20220321/227_db9bfd00/1200k/hls/mixed.m3u8?token=CswMeJ337ZQXusqE5Yfd6Q&expires=1739545423





