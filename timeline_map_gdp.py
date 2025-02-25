"""
要构建时间线性柱状图
要导入charts options 包里面的bar Timeline

"""
from pyecharts.charts import Bar , Timeline
from pyecharts.options import *
from pyecharts.globals import ThemeType # 设置图表主题

bar=Bar()
bar.add_xaxis(['中国','美国','英国'])
bar.add_yaxis('gdp',[50,60,30],label_opts=LabelOpts(position='right'))
bar.reversal_axis()


bar2=Bar()
bar2.add_xaxis(['中国','美国','英国'])
bar2.add_yaxis('gdp',[55,59,35],label_opts=LabelOpts(position='right'))
bar2.reversal_axis()

bar3=Bar()
bar3.add_xaxis(['中国','美国','英国'])
bar3.add_yaxis('gdp',[59,61,40],label_opts=LabelOpts(position='right'))
bar3.reversal_axis()

bar4=Bar()
bar4.add_xaxis(['中国','美国','英国'])
bar4.add_yaxis('gdp',[63,60,42],label_opts=LabelOpts(position='right'))
bar4.reversal_axis()

bar5=Bar()
bar5.add_xaxis(['中国','美国','英国'])
bar5.add_yaxis('gdp',[66,63,48],label_opts=LabelOpts(position='right'))
bar5.reversal_axis()

"""
Timeline()对象提供线性时间功能
把两张表分别放在两个时间点上
再用add_schema（）来添加自动播放
"""
tl=Timeline(
    {"theme":ThemeType.LIGHT} # 添加高亮主题
)

tl.add(bar,"2021") # 添加在不同时间线
tl.add(bar2,"2022")
tl.add(bar3,'2023')
tl.add(bar4,'2024')
tl.add(bar5,'2025')

tl.add_schema(
    play_interval=1, # 播放时间间隔 1000ms
    is_timeline_show=True, # 显示时间线
    is_auto_play=True,  # 自动播放
    is_loop_play=True   # 循环播放
)




tl.render("基础柱状线性时间图绘制.html")

























