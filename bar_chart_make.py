from pyecharts.charts import Bar
from pyecharts.options import TitleOpts,LabelOpts

bar=Bar()
bar.add_xaxis(['中国','美国','英国'])
bar.add_yaxis('gdp',[30,20,10],label_opts=LabelOpts(position='right'))
# label_opts可以更改图中数据标示的位置
bar.reversal_axis() # reversal_axis()可以反转坐标轴
bar.set_global_opts(
    title_opts=TitleOpts(title="中美英三国GDP",pos_left='center',pos_bottom='1%')
)

bar.render('1960-2019动态全球前8GDP展示图.html')









