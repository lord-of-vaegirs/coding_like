

# /Users/lxjarctane2/Desktop/WechatIMG1286.jpg

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np

# 加载背景图片
background_img_path = "/Users/lxjarctane2/Desktop/WechatIMG1286.jpg"  # 替换为您的图片路径
background_img = mpimg.imread(background_img_path)

# 获取图片分辨率
img_height, img_width, _ = background_img.shape

# 创建绘图区域，设置与背景图片比例相匹配的坐标系
fig, ax = plt.subplots(figsize=(img_width / 100, img_height / 100))

# 显示背景图片
ax.imshow(background_img, extent=[0, img_width, 0, img_height], zorder=0)

# 添加绘图内容，确保内容位于背景图片上层
x = np.linspace(100, img_width - 100, 500)  # 示例数据：x 坐标
y = (img_height / 2) + (img_height / 4) * np.sin(2 * np.pi * x / img_width)  # 示例数据：正弦波
ax.plot(x, y, color='red', linewidth=2, label='Sine Wave', zorder=2)  # 绘制曲线

# 设置坐标范围，确保背景图片与绘图内容对齐
ax.set_xlim(0, img_width)
ax.set_ylim(0, img_height)

# 显示网格线和坐标轴
ax.grid(color='white', linestyle='--', linewidth=0.5, zorder=1)  # 网格线
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_title("Plot with Background Image")

# 显示图例（可选）
ax.legend()

# 调整布局并显示
plt.tight_layout()
plt.show()




