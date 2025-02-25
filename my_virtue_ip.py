"""
当我们需要短时间内取得大量数据的时候
如果只用一个ip，会被查封
只能使用多个ip，同时请求
站大爷 免费代理 匿名选择透明或者未知
"""


# 58.23.152.29:7080 透明
# 111.1.61.47:3128 透明
# 39.108.2.73:3838 透明
# 218.60.8.83:3129 透明


import requests

proxies={
    "http":"https://58.23.152.29:7080"
}

resp=requests.get("https://www.baidu.com",proxies=proxies)

resp.encoding='utf-8'

print(resp.text)







