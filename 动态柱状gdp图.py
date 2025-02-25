from pyecharts.charts import Bar,Timeline
from pyecharts.options import *
"""
列表中的sort函数
用于每个元素为列表、元组的列表的排序
sort(key=func(),reverse=True/False)
key后面的函数作为排序依据
reverse就是表示是否倒序

key函数可以写成如下格式

def func(ele):
    return ele[1]

表示按照每个元素列表里面第1个元素来排序

key 也可以写成匿名函数形式lambda
key=lambda ele:ele[1]

"""

my_list=[['a',33],['b',55],['c',11]]

def func(ele):
    return ele[1]

# my_list.sort(key=func,reverse=True)

my_list.sort(key=lambda ele:ele[1],reverse=False)

# print(my_list)

"""
最终效果图需要有：
gdp数据处理为亿级
有时间轴，按照年份为时间轴的点
x轴和y轴反转，同时每一年的数据只要前8名国家
有标题，标题的年份会动态更改
设置主题为LIGHT
"""

f=open("/Users/lxjarctane2/Downloads/资料/可视化案例数据/动态柱状图数据/1960-2019全球GDP数据.csv","r",encoding='GB2312')
data_lines=f.readlines()
# print(type(data_lines))
f.close()
# 把第一行无用数据删掉
data_lines.pop(0)

# 数据转换成字典格式储存 年份为key 所有国家的名称和gdp为value
data_dict=dict()
year=1960
for i in data_lines:
    year=int(i.split(',')[0])
    country=i.split(',')[1]
    gdp=float(i.split(',')[2])
    try:
        data_dict[year].append((country,gdp))
    except KeyError:
        data_dict[year]=[]
        data_dict[year].append((country,gdp))

# print (data_dict)
# 排序年份 先取出所有的key 再放入for循环绘图
sorted_year_list=sorted(data_dict.keys())
# print(sorted_year_list)

timeline=Timeline(
    {"theme":"LIGHT"}
)

for i in sorted_year_list:
    data_dict[i].sort(key=lambda ele:ele[1],reverse=True)
    #先排序每一年的list 保证前八个是前八名
    map_data_list=data_dict[i][:8]
    x_data=[]
    y_data=[]
    for j in map_data_list:
        x_data.append(j[0])
        y_data.append(j[1])

    bar=Bar()
    x_data.reverse()
    y_data.reverse()
    bar.add_xaxis(x_data)

    bar.add_yaxis("各国gdp(亿)",y_data,label_opts=LabelOpts(position="right"))

    bar.reversal_axis()

    bar.set_global_opts(
        title_opts=TitleOpts(title="1960-2019年全球前8国家gdp")
    )

    timeline.add(bar,str(i))




timeline.add_schema(
    play_interval=1000,
    is_timeline_show=True,
    is_auto_play=True,
    is_loop_play=True

)

timeline.render('1960-2019动态全球前8GDP展示图.html')






































