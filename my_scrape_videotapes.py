"""
视频网站处理视频
用户上传->转码（2k 标清 ...）
->切片处理（把单个文件拆分成极多的小份，用户将进度条切换到哪里，就加载进度条附近的小份文件即可）

需要一个文件 记录视频切片的顺序 和 存放的路径

M3U M3U8文件 就是保存这些信息的一个文件
.ts 是切片文件的后缀

想要抓取一个视频
1. 找到m3u8文件
2. 通过m3u8下载到ts文件
3. 用各种手段把ts文件合并为一个mp4文件

"""
import io

"""
流程：
拿到页面源代码 
从源代码里面提取m3u8的url
下载m3u8文件
读取m3u8 下载视频
合并视频

"""
import requests
import re
import aiohttp
import aiofiles
import asyncio

header={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
}


obj=re.compile(r'<div class="stui-pannel_bd stui-pannel-box-none">.*?<source id="source" src="(?P<m3u8>.*?)"',re.S)
# 提取m3u8地址
url='https://www.yitutrend.com/vp-ectid/126562-1.html'

resp=requests.get(url,headers=header)

m3u8_url=obj.search(resp.text).group('m3u8')

print(m3u8_url)
resp.close()

resp2=requests.get(m3u8_url,headers=header)

with open('大奉打更人.m3u8',mode='wb') as f:
    f.write(resp2.content)

resp2.close()

print('over!')


n = 1
with open('大奉打更人.m3u8', mode='r', encoding='utf-8') as f:
    for i in f:
        line = i.strip()
        if line.startswith('#'):
            continue
        # 下载视频片段
        resp3=requests.get(line)
        f=open(f'video/{n}.ts',mode='wb')
        f.write(resp3.content)
        f.close()
        resp3.close()
        n+=1
        print('完成了1个')










