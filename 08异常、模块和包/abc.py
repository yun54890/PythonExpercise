from pyecharts import options as opts
from pyecharts.charts import Line
import random

# 1. 生成随机数据
# X轴：1~12月份
x_data = [f"{i}月" for i in range(1, 13)]
# Y轴两组随机数据，范围 100 ~ 600
y_data1 = [random.randint(100, 600) for _ in range(12)]
y_data2 = [random.randint(100, 600) for _ in range(12)]

# 2. 创建折线图
line_chart = (
    Line(init_opts=opts.InitOpts(width="1000px", height="600px"))
    # X轴数据
    .add_xaxis(x_data)
    # 第一条折线
    .add_yaxis("产品A销量", y_data1, markpoint_opts=opts.MarkPointOpts(
        data=[opts.MarkPointItem(type_="max"), opts.MarkPointItem(type_="min")]
    ))
    # 第二条折线
    .add_yaxis("产品B销量", y_data2, markline_opts=opts.MarkLineOpts(
        data=[opts.MarkLineItem(type_="average")]
    ))
    # 全局配置：标题、坐标轴、提示框
    .set_global_opts(
        title_opts=opts.TitleOpts(title="月度销量随机折线图", subtitle="随机生成测试数据"),
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=30)),
        yaxis_opts=opts.AxisOpts(name="销量(件)"),
        tooltip_opts=opts.TooltipOpts(trigger="axis"),
        legend_opts=opts.LegendOpts(pos_left="center", pos_top="bottom")
    )
)

# 3. 生成html文件，打开即可查看图表
line_chart.render("随机折线图.html")
print("图表已生成：随机折线图.html")
