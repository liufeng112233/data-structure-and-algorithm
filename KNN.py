#  shuju
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

# matplotlib inline
# 原始数据
data = [[1, 0.9], [1, 1], [0.1, 0.2], [0, 0.1]]
labels = ['A', 'A', 'B', 'B']
test_data = [[0.1, 0.3]]
# 绘制原始数据散点图
print("------------------------数据准备----------------------")
print("原始数据图像绘制...")
for i in range(len(data)):
    plt.scatter(data[i][0], data[i][1], color='b')
plt.scatter(test_data[0][0], test_data[0][1], color='r')
plt.show()
# 测试数据x=(0.1,0.3)
# 采用欧氏距离进行计算
print("------------------------距离计算----------------------")
x = [[0.1, 0.3]]
distance = []
labels_vz = []
for i in range(len(data)):
    d = 0
    d = sqrt((x[0][0] - data[i][0]) ** 2 + (x[0][1] - data[i][1]) ** 2)
    distance.append(d)
    labels_vz.append(i)
print("计算的距离为：\n", distance)
print("现在对应的标签位置为：\n", labels_vz)
# 按照升序排序，并取距离最小的前3个
print("-----------------------距离排序-----------------------")
for i in range(len(data) - 1):
    for j in range(i + 1, len(data)):
        if distance[i] > distance[j]:
            distance[i], distance[j] = distance[j], distance[i]
            labels_vz[i], labels_vz[j] = labels_vz[j], labels_vz[i]
print("排序后的距离为：\n", labels_vz)
print("取距离最近的3个值：", distance[0:3])
# 进行投票表决
print("-----------------------表决投票-----------------------")
A = 0
B = 0
for i in range(len(labels_vz[0:3])):
    if labels[labels_vz[i]] == 'A':
        A += 1
    else:
        B += 1
print("投票为A的数量为：", A)
print("投票为B的数量为：", B)
print("\n对照初始图中红色点（测试点）与前两个标签为A的离的最近，所以我们的计算与图中所呈现的绘图一致")
