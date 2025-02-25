"""
可视化地图

"""

from pyecharts.charts import Map
from pyecharts.options import VisualMapOpts

map=Map()
# 准备地图对象

#准备数据
data=[
    ('北京市',99),
    ('上海市',98),
    ('河南省',90),
    ('湖南省',100),
    ('广西壮族自治区',93),

]

# 添加数据
map.add('测试数据',data,"china")

# 添加全局配置
map.set_global_opts(
    visualmap_opts=VisualMapOpts(
        is_show=True,
        is_piecewise=True,
        pieces=[
            {'min':1,'max':9,'label':'1-9人','color':'#CCFFFF'},
            {'min':10,'max':99,'label':'10-99人','color':'#FFFF99'},
            {'min':100,'max':499,'label':'100-499人','color':'#FF9966'},
            {'min':500,'max':999,'label':'500-999人','color':'#FF6666'},
            {'min':1000,'max':1999,'label':'1000-1999人','color':'#CC3333'}
        ]
    )
)
# 视觉映射添加 show展示 piecewise打开手动校准 pieces改变具体映射范围和颜色
# 颜色对照表在ab173站 前端上

# 绘图
map.render()





