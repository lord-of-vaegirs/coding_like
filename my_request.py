# 爬虫 request

# 程序模拟浏览器，输入网址 从网址获取资源和内容

from urllib.request import urlopen

url='http://www.baidu.com'
resp=urlopen(url)


with open("mybaidu.html",mode='w',encoding='UTF-8') as f: # 将请求到的源代码保存到mybaidu.html文件里面了
    f.write(resp.read().decode('utf-8'))
resp.close()

# 请求过程剖析：
# 1.服务器渲染：服务器把html骨架和数据整合在一起，
#  统一返回给浏览器 页面源代码里面能看到数据
# 2.客户端渲染： 第一次请求只要到了html骨架，第二次请求拿到数据，进行数据展示，
#  在页面源代码中看不到数据
# import requests
# query=input('请输入一个你想搜索的名称')
#
# url=f'https://www.sogou.com/web?query={query}'
#
#
# dic={
#     'User Agent':"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:134.0) Gecko/20100101 Firefox/134.0"
# }
# resp=requests.get(url,headers=dic)
# print(resp)
# print(resp.text)



# requests爬取翻译网站
# import requests
#
# url="https://fanyi.baidu.com/sug" # post请求
# s=input('请输入你要翻译的英文单词\n')
# dat={
#     "kw":s # keyword
#
# }
#
# resp=requests.post(url,data=dat) # post请求传入参数是用data
# print(resp.json()) # 将服务器产生的内容直接转换成json数据
# import requests
# # from datetime import datetime
# import json
# import pandas as pd
# # get请求有参数时 需要重新封装参数
# param={
#     "type": "24",
#     "interval_id": "100:90",
#     "action": "",
#     "start": "0",
#     "limit": "20"
# }
#
# headers={
#     "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36"
# }
#
# url='https://movie.douban.com/j/chart/top_list'
# resp=requests.get(url=url,params=param,headers=headers) # get请求传入参数用params
# # print(resp.request.url)
# # print(resp.request.hearder)
# # print(resp.text) # 如果输出是空白 就是被反爬了
# print(resp.json())
# print(type(resp.json()))
# data_lt=resp.json()
# resp.close() # 要关！！！否则多了会被封
# # with open('豆瓣喜剧评分排行榜.json','w') as f:
# #     f.write(str(data))
# #     f.flush()
# #     f.close()
#
# """
# {'rating': ['9.5', '50'],
# 'rank': 1,
# 'cover_url': 'https://img3.doubanio.com/view/photo/s_ratio_poster/public/p2578474613.jpg',
#  'is_playable': True,
#  'id': '1292063',
#  'types': ['剧情', '喜剧', '爱情', '战争'],
#  'regions': ['意大利'],
#  'title': '美丽人生',
#  'url': 'https://movie.douban.com/subject/1292063/',
#   'release_date': '2020-01-03',
#   'actor_count': 29,
#   'vote_count': 1417324,
#    'score': '9.5',
#    'actors': ['罗伯托·贝尼尼', '尼可莱塔·布拉斯基', '乔治·坎塔里尼', '朱斯蒂诺·杜拉诺', '赛尔乔·比尼·布斯特里克', '玛丽萨·帕雷德斯', '霍斯特·布赫霍尔茨', '利迪娅·阿方西', '朱利亚娜·洛约迪切', '亚美利哥·丰塔尼'],
#    'is_watched': False}
# """
# title_lt=[]
# rank_lt=[]
# type_lt=[]
# region_lt=[]
# url_lt=[]
# release_date_lt=[]
# actor_count_lt=[]
# vote_count_lt=[]
# score_lt=[]
# main_actors_lt=[]
#
# # date_format='%Y-%m-%d'
#
# for i in data_lt:
#     title_lt.append(i['title'])
#     rank_lt.append(i['rank'])
#     type_lt.append(i['types'])
#     region_lt.append(i['regions'])
#     url_lt.append(i['url'])
#     release_date_lt.append(i['release_date'])
#     actor_count_lt.append(i['actor_count'])
#     vote_count_lt.append(i['vote_count'])
#     score_lt.append(i['score'])
#     main_actors_lt.append(i['actors'])
#
# data={
#     '电影名': title_lt,
#     '排名': rank_lt,
#     '评分': score_lt,
#     '类型':type_lt,
#     '国家/地区':region_lt,
#     '上映日期': release_date_lt,
#     '主演':main_actors_lt,
#     '参评人数':vote_count_lt,
#     '演员总数':actor_count_lt,
#     '网址':url_lt
# }
#
# df=pd.DataFrame(data)
#
# df.to_excel('/Users/lxjarctane2/Desktop/豆瓣评分.xlsx')





