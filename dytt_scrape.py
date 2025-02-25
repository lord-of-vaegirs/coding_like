import requests
import re
import time
import pandas as pd



domain="https://www.dytt89.com/"
header={
    'User-Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}
resp=requests.get(domain,verify=False,headers=header) # 去除了ssl证书验证再发送请求
resp.encoding='gb2312' # 使用网址的中文编码

# print(resp.text)

obj1=re.compile(r"2025必看热片.*?<ul>(?P<ul>.*?)</ul>",re.S)
obj2=re.compile(r"<a href='(?P<href>.*?)'",re.S)
obj3=re.compile(r'◎片　　名(?P<name>.*?)<br />.*?<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download_url>.*?)"',re.S)



res1=obj1.finditer(resp.text)
child_href_list=[]
for i in res1:
    url=i.group('ul')
    res2=obj2.finditer(url)
    for it in res2:
        child_href=domain+it.group('href').strip('/') # 每个子页面的url都拿到了
        child_href_list.append(child_href)
        # print(it.group('href'))

# <a></a> 超链接   <a href='https://www.xxy.com/' title="测试网站">测试网站</a> 就会把“测试网站”四个字变成超链接
# 所以想要提取链接，就提取herf就行
name_lt=[]
url_lt=[]
for href in child_href_list:
    time.sleep(0.5)
    child_resp=requests.get(href,verify=False,headers=header)
    child_resp.encoding='gb2312'
    # print(child_resp.text)
    res3=obj3.search(child_resp.text)
    name_lt.append(res3.group('name').strip())
    url_lt.append(res3.group('download_url'))
    # print(res3.group('name').strip())
    # print(res3.group('download_url'))
    child_resp.close()
    # break

resp.close()

data={
    '电影名': name_lt,
    '下载链接':url_lt
}


df=pd.DataFrame(data)

df.to_excel('/Users/lxjarctane2/Desktop/dytt.xlsx')














