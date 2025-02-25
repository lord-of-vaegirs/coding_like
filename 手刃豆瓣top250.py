# 拿到代码，用re提取
import requests
import re
import csv
import pandas as pd
import time

# name year director main_actor score vote_count quote
name_lt=[]
year_lt=[]
director_lt=[]
main_actor_lt=[]
score_lt=[]
vote_count_lt=[]
quote_lt=[]


for i in range(0,249,25):
    time.sleep(1)

    url = f'https://movie.douban.com/top250?start={i}&filter='

    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36'
    }

    resp = requests.get(url, headers=header)
    # print(resp.text)
    resp.close()
    page_content = resp.text

    obj = re.compile(
        r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">.*?导演: (?P<director>.*?)&nbsp;&nbsp;&nbsp;主演: (?P<main_actor>.*?)'
        r'<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
        r'.*? <span property="v:best" content="10.0">.*?<span>(?P<vote_count>.*?)</span>.*?</div>.*?<p class="quote">.*?<span class="inq">(?P<quote>.*?)</span>',
        re.S)

    res = obj.finditer(page_content)

    for i in res:
        name_lt.append(i.group('name').strip())
        year_lt.append(i.group('year').strip())
        director_lt.append(i.group('director').strip())
        main_actor_lt.append(i.group('main_actor').strip())
        score_lt.append(i.group('score').strip())
        vote_count_lt.append(i.group('vote_count').strip())
        quote_lt.append(i.group('quote').strip())

print('over!!!')

data={
    '剧名':name_lt,
    '上映年份':year_lt,
    '评分':score_lt,
    '导演':director_lt,
    '主演':main_actor_lt,
    '投票人数':vote_count_lt,
    '格言':quote_lt
}

df=pd.DataFrame(data)

df.to_excel('/Users/lxjarctane2/Desktop/豆瓣top250.xlsx')












# for i in res:
#     print(i.group('name'),end=' ')
#     print(i.group('year').strip(),end=' ')
#     print(i.group('score').strip(),end=' ')
#     print(i.group("vote_count").strip(),end=' ')
#     print(i.group('quote').strip())

# csv 格式数据保存
# f=open('data.csv',mode='w',encoding='UTF-8')
# csvwriter=csv.writer(f)
# for i in res:
#     dic=i.groupdict()
#     dic['year']=dic['year'].strip()
#     csvwriter.writerow(dic.values())
# f.close()




