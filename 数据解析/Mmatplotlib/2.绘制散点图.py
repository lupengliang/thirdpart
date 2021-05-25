"""
1.edgecolor='none'删除点的轮廓
2.c='red'自定义颜色
3.使用颜色映射：渐变
4.自动保存图片
"""
import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

# plt.scatter(x_values, y_values, c='red', edgecolors='none', s=40)
# plt.scatter(x_values, y_values, c=(0, 0, 0.8), edgecolors='none', s=40)  # 自定义颜色
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)  # 颜色映射

# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=14)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

plt.show()

plt.savefig('square_plot.png', bbox_inches='tight')  # 保存图片
