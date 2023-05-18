from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics import renderPDF

from pyecharts import options as opts
from pyecharts.charts import Bar, Line

# 创建PDF文档
doc = SimpleDocTemplate("report.pdf", pagesize=letter)

# 定义样式
styles = getSampleStyleSheet()
title_style = styles["Heading1"]
subtitle_style = styles["Heading2"]
line_style = ParagraphStyle("Line", parent=styles["Normal"], spaceAfter=10)
table_style = TableStyle([
    ("BACKGROUND", (0, 0), (-1, 0), colors.gray),
    ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
    ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
    ("FONTSIZE", (0, 0), (-1, 0), 12),
    ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
    ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
    ("TEXTCOLOR", (0, 1), (-1, -1), colors.black),
    ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
    ("FONTSIZE", (0, 1), (-1, -1), 10),
    ("ALIGN", (0, 0), (-1, -1), "LEFT"),
])

# 定义数据
title_img = "logo.png"  # 标题图片路径
title_text = "PDF报告标题"
subtitle_text = "PDF报告副标题"
basic_info_title = "基本信息"
basic_info_data = [
    ["姓名", "张三"],
    ["年龄", "30"],
    ["性别", "男"],
]
collect_info_title = "采集信息"
collect_info_data = [
    ["日期", "数值"],
    ["2023-05-01", "100"],
    ["2023-05-02", "150"],
    ["2023-05-03", "200"],
]
sleep_stage_title = "睡眠分期"
sleep_stage_data = [
    ["日期", "分期"],
    ["2023-05-01", "浅睡眠"],
    ["2023-05-02", "深睡眠"],
    ["2023-05-03", "REM睡眠"],
]
heart_rate_title = "心率统计"
heart_rate_data = [
    ["日期", "心率"],
    ["2023-05-01", "80"],
    ["2023-05-02", "90"],
    ["2023-05-03", "85"],
]
heart_rate_curve_data = [
    (1, 80),
    (2, 90),
    (3, 85),
]

# 构建PDF内容
elements = []

# 标题部分
title_img = Image(title_img, width=2 * inch, height=1 * inch)
elements.append(title_img)
elements.append(Spacer(1, 12))
elements.append(Paragraph(title_text, title_style))
elements.append(Paragraph(subtitle_text, subtitle_style))
elements.append(Spacer(1, 12))

# 基本信息
elements.append(Paragraph(basic_info_title, subtitle_style))
elements.append(Drawing(1, 0.1 * inch))
elements.append(Spacer(1, 12))
table = Table(basic_info_data)
table.setStyle(table_style)
elements.append(table)
elements.append(Spacer(1, 12))

# 采集信息
elements.append(Paragraph(collect_info_title, subtitle_style))
elements.append(Drawing(1, 0.1 * inch))
elements.append(Spacer(1, 12))
table = Table(collect_info_data)
table.setStyle(table_style)
elements.append(table)
elements.append(Spacer(1, 12))

# 睡眠分期
elements.append(Paragraph(sleep_stage_title, subtitle_style))
elements.append(Drawing(1, 0.1 * inch))
elements.append(Spacer(1, 12))
table = Table(sleep_stage_data)
table.setStyle(table_style)
elements.append(table)
elements.append(Spacer(1, 12))

# 带小图标的柱状图
# bar_data = [data[1] for data in collect_info_data[1:]]
# x_data = [data[0] for data in collect_info_data[1:]]
# bar = (
#     Bar()
#     .add_xaxis(x_data)
#     .add_yaxis("数值", bar_data)
#     .set_global_opts(title_opts=opts.TitleOpts(title="采集信息统计"))
# )
# bar.render("bar.html")
# elements.append(Paragraph("采集信息统计", subtitle_style))
# elements.append(Drawing(1, 0.1 * inch))
# elements.append(Spacer(1, 12))
# elements.append(Image("bar.html", width=6 * inch, height=3 * inch))
# elements.append(Spacer(1, 12))

# # 心率统计
# elements.append(Paragraph(heart_rate_title, subtitle_style))
# elements.append(Drawing(1, 0.1 * inch))
# elements.append(Spacer(1, 12))
# table = Table(heart_rate_data)
# table.setStyle(table_style)
# elements.append(table)
# elements.append(Spacer(1, 12))

# # 心率曲线图
# x_data = [data[0] for data in heart_rate_curve_data]
# y_data = [data[1] for data in heart_rate_curve_data]
# line = (
#     Line()
#     .add_xaxis(x_data)
#     .add_yaxis("心率", y_data)
#     .set_global_opts(title_opts=opts.TitleOpts(title="心率曲线"))
# )
# line.render("line.html")
# elements.append(Paragraph("心率曲线", subtitle_style))
# elements.append(Drawing(1, 0.1 * inch))
# elements.append(Spacer(1, 12))
# elements.append(Image("line.html", width=6 * inch, height=3 * inch))
# elements.append(Spacer(1, 12))

# 生成PDF
doc.build(elements)

