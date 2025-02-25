import requests
from lxml import etree

header={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}

url="https://www.zbj.com/fw/?k=saas"
resp=requests.get(url,headers=header)
# print(resp.text)
resp.close()

html=etree.HTML(resp.text) # 直接解析html源码

divs=html.xpath('//*[@id="__layout"]/div/div[3]/div/div[4]/div/div[2]/div/div[2]/div')
for div in divs:
    price = div.xpath(f'./div/div[3]/div[1]/span/text()')[0].strip('¥')
    name = "saas".join(div.xpath(f'./div/div[3]/div[2]/a/span/text()')) # 用saas拼接中间空缺的部分
    company_name=div.xpath('./div/div[5]/div/div/div/text()')[0]
    score=div.xpath('./div/div[5]/div/div/span/text()')
    print(score)
# //*[@id="__layout"]/div/div[3]/div[1]/div[4]/div/div[2]/div/div[2]/div[1]/div/div[5]/div/div/span/text()
# score 的 xpath




























