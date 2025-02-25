# 拿到主页面源代码，提取子页面的链接地址href
# 通过href拿到子页面内容，从子页面中找到图片的下载地址。img->src
# 下载图片

import requests
from bs4 import BeautifulSoup
import time

url="https://www.umei.cc/bizhitupian/weimeibizhi/"

resp=requests.get(url)

# print(resp.text)

main_page=BeautifulSoup(resp.text,"html.parser")

p=main_page.find("div",class_="Clbc_r_cont").find_all('li',class_="Clbc_list_dixx")

graph_lt=[]
# https://www.umei.cc/bizhitupian/weimeibizhi/245899.htm
for i in p:
    suburl=i.find_all("a")[0].get('href')
    time.sleep(1)
    resp2=requests.get('https://www.umei.cc'+suburl)
    resp2.encoding='utf-8'
    child_page=BeautifulSoup(resp2.text,"html.parser")
    pp=child_page.find("div",class_="big-pic")
    res=pp.find("img").get("src")
    graph_lt.append(res)

print(graph_lt)

for i in graph_lt:
    img_resp = requests.get(i)
    # img_resp.content # 这里拿到了图片的字节
    img_name=i.split('/')[-1]
    with open(img_name,mode='wb') as f:
        f.write(img_resp.content) # 图片内容写入文件






