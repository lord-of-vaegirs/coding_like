# html语法  <标签 属性="值" 属性="值">被标记的内容</标签>

import requests
from bs4 import BeautifulSoup
import csv

header={
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
}

url="http://www.hksclzjt.com/groceries/index"

f=open('vege_price.csv',mode="w")
csvwriter=csv.writer(f)

resp=requests.get(url,headers=header)
resp.encoding='utf-8'
print(resp.text)

# 解析数据
# 1.把页面源代码交给BS处理 生成bs对象
page=BeautifulSoup(resp.text,"html.parser") # 指定html解析器
# 2.从bs对象中查找数据
# find(标签，属性=值)
# find_all(标签，属性=值)
# table=page.find("table",class_="bjtbl")
table=page.find_all('table')
tab1=table[0]
tab2=table[1]

tb_lt=[]

tb_lt.extend(tab1.find_all("tr")[1:])
tb_lt.extend(tab2.find_all("tr")[1:])

for i in tb_lt:
    p=i.find_all("td")
    date=p[0].text
    name=p[1].text
    price=p[2].text
    csvwriter.writerow([date,name,price])









