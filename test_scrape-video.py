import re
import requests
import aiohttp
import aiofiles
import asyncio

header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
}


def get_first_m3u8(url):
    obj = re.compile(
        r'<div class="stui-player__video clearfix">.*?<script type="text/javascript">.*?"vod_class":".*?","url":"(?P<url2>.*?)".*?',re.S)
    resp = requests.get(url, headers=header)
    return obj.search(resp.text).group('url2') if obj.search(resp.text) else None


def download_m3u8(url, output_dir='.', filename=None):
    if not filename:
        filename = url.split('/')[-1]
    with open(f'{output_dir}/{filename}', 'wb') as f:
        resp = requests.get(url, headers=header)
        for chunk in resp.iter_content(chunk_size=8192):
            f.write(chunk)


async def download_ts(url, output_dir='.', filename=None, concurrency=5):
    if not filename:
        filename = url.split('/')[-1]
    async with aiohttp.ClientSession() as session:
        async for _ in range(concurrency):
            await asyncio.sleep(0.1)
            try:
                async with session.get(url) as response:
                    content = await response.content
                    async with aiofiles.AsyncIOFile.open(f'{output_dir}/{filename}', 'wb') as f:
                        await f.write(content)
                        print(f"Downloaded {filename}")
            except Exception as e:
                print(f"Error downloading {filename}: {e}")


async def process_m3u8(url, output_dir='.', max_workers=5):
    m3u8_urls = []
    async with aiohttp.ClientSession() as session:
        async for line in await session.get(str(url), headers=header):
            lines = line.decode().splitlines()
            for line in lines:
                match = re.match(r'^\s*#[0-9][-.]+\.ts$', line.strip())
                if match:
                    m3u8_urls.append(match.group(1))
        print(f"Found {len(m3u8_urls)} TS files to download")
        if not m3u8_urls:
            return
        with asyncio.gather(
                *[download_ts(t, output_dir=output_dir, filename=t) for t in m3u8_urls]
        ):
            await asyncio.sleep(1)


async def main():
    # 假设video_url是你需要下载的M3U8文件的URL
    video_url = "https://example.com/video.m3u"
    m3u8_output = "m3u_output"

    if not video_url:
        print("Please provide a valid M3U8 URL")
        return

    # 下载第一个M3U8文件
    first_m3u8_url = await get_first_m3u8(video_url)
    if not first_m3u8_url:
        print("Could not extract M3U8 URL from the provided page.")
        return

    # 下载对应的TS files
    await process_m3u8(first_m3u8_url, output_dir="downloads", max_workers=5)


if __name__ == '__main__':
    asyncio.run(main())