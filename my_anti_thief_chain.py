# 处理有防盗链措施的视频
# 拿到contID
# 拿到videostatus返回的json->srcURL
# 下载视频
import requests



url='https://www.pearvideo.com/video_1797596'
contID=url.split('_')[1] # 拿到contid

header={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36",
    "Referer": url # 这就是防盗链 它会找网站的溯源 "https://www.pearvideo.com/video_1797596"
}


videostatusURL=f'https://www.pearvideo.com/videoStatus.jsp?contId={contID}&mrd=0.6726367080982871'

resp=requests.get(videostatusURL,headers=header)

dic=resp.json()

srcurl=dic["videoInfo"]["videos"]["srcUrl"]

sys_time=dic["systemTime"]

# 处理srcurl
srcurl=srcurl.replace(sys_time,f"cont-{contID}")

print(srcurl)

# 下载视频

with open('PanZhanle.mp4',mode="wb") as f: # 二进制数据写入wb
    f.write(requests.get(srcurl).content) # 将链接内容写入


























