"""
numpy 库方法
"""
# 1.一维数组创建
import numpy as np
print(np.array([1, 2, 3, 4, 5]))
# 结果：[1 2 3 4 5]


# 2. 二维数组创建
import numpy as np
print(np.array([[1, 2, 3], [4, 5, 6]]))
# 结果：[[1 2 3]
#       [4 5 6]]


# 3. 使用matplatlib.pyplot获取一个numpy数组，数据来源于一张图片
# 操作该numpy数据，该操作会同步到图片中
import matplotlib.pyplot as plt
img_arr = plt.imread('./cat.jpg')  # 将图片变为三维数组
print(plt.imshow(img_arr))  # 将图片的三维数组还原为图片
# 结果：返回三维数组


# 4. 使用np的routines函数创建
# 4.1. np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None) 等差数列
import numpy as np
print(np.linspace(1, 100, num=10))  # 只能返回一维数组

# 4.2. np.arrange([start,]stop,[step,]dtye=None) 等差数列
import numpy as np
print(np.arange(1, 100, 2))  # 只能返回一维数组

# 4.3. np.random.randint(low, high=None, size=None, dtype='l')
# 随机原是：随机因子：表示一个无时无刻都在变化的数值
import numpy as np
# 固定随机因子： np.random.seed(10)
print(np.random.randint(1, 100, size=(4, 5)))  # 产生任意维度的数组 eg:4维5列

# 4.4. np.random.random(size=(5,3))
import numpy as np
print(np.random.random(size=(5, 3)))  # 返回 0~1 之间任意维度的数组 eg:5维3列


# 5. ndarray的属性
# 5.1 ndim:返回数组的维度
print(img_arr.ndim)

# 5.2 shape:返回数组的形状（各维度的长度）
print(img_arr.shape)

# 5.3 size:返回数组的总长度
print(img_arr.size)

# 5.4 dtype:返回数组的元素类型
print(img_arr.dtype)


# 6. ndarray的基本操作
# 6.1 索引
arr = np.random.randint(60, 120, size=(6, 8))
print(arr[1])  # 取第1行
print(arr[1][2])  # 第1行的第3列

# 6.2 切片
# 6.2.1 获取二维数组前两行
print(arr[0:2])

# 6.2.2 获取二维数组前两列
print(arr[:, 0:2])  # 应用了逗号的机制，逗号左边为第一个维度，右边为第二个维度

# 6.2.3 获取二维数组前两行和前两列数据
print(arr[0:2, 0:2])

# 6.2.4 数组的行倒序
print(arr[::-1])

# 6.2.4 数组的列倒序
print(arr[:, ::-1])

# 6.2.5 图片反转 在jupyter中可以实现
# print(plt.show(img_arr[:, ::-1, :]))


# 7. 变形： arr.reshape() 参数: tuple
# 7.1 将一维数组变形成多维数组
print(arr.reshape((12, 4)))  # 6行8列 变为了 12行4列

# 7.2 将多维数组变形成一维数组
print(arr.reshape((48,)))


# 8. 级联 np.concatenate()
# 8.1 一维、二维数组的级联，实际操作中级联多为二维数组 例：2维
np.concatenate((arr, arr), axis=1)  # 0表示列 1表示行

# 8.2 合并两张照片 例：3维
arr_3 = np.concatenate((img_arr, img_arr, img_arr), axis=1)  # 0表示列 1表示行 2表示z
arr_9 = np.concatenate((arr_3, arr_3, arr_3), axis=0)
plt.imshow(arr_9)  # 在jupyter中展示成功


# 9. ndarray的聚合操作
# 9.1 求和np.sum 例：2维数组
arr.sum(axis=None)

# 9.2 多
# 9.3 多
# 9.4 多


# 10. ndarray 排序
# 10.1 快速排序
arr.sort(axis=0)  # 0: 对列排序 1：行 None：所有


# 11. 裁减图片
plt.imshow(img_arr[50:400, 100:370, :])  # 使用切片 列，行，颜色


