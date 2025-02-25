"""
构建折线图
首先导入 构建相应的图对象
添加数据


添加全局配置
添加系列配置


render生成图像
"""
from pyecharts.charts import Line
# 导入折线图
from pyecharts.options import TitleOpts,LegendOpts,ToolboxOpts,TooltipOpts,VisualMapOpts
# 导入全局配置所在包

line = Line()
# 创建折线图对象
line.add_xaxis(['中国','美国','英国'])
# 给折线图添加了x轴的数据
line.add_yaxis("gdp",[30,10,20])
# 给折线图添加了y轴数据



# 设置全局配置 set_global_opts()
# title_opts 标题配置 利用TitleOpts方法 规定title='名称' pos_left="center"居中展示 或者通过百分比来控制 pos_bottom='1%' 控制上下位置
# legend_opts 图例配置
# toolbox_opts 工具箱配置
# visualmap_opts 视觉映射配置
# tooltip_opts 提示框配置
line.set_global_opts(
    title_opts=TitleOpts(title='gdp showcase',pos_left="center",pos_bottom='1%'),
    legend_opts=LegendOpts(is_show=True),
    toolbox_opts=ToolboxOpts(is_show=True),
    visualmap_opts=VisualMapOpts(is_show=True),
    tooltip_opts=TooltipOpts(is_show=True)
)
# 具体的全局配置给如何做，请前往pyecharts.org 全局配置项 查看


line.render()
# 使用render方法生成图像

# www.ab173.com懒人工具查看json数据视图，可以用来分析层级







