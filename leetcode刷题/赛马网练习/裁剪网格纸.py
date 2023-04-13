# -*- codeing = utf-8 -*-
# @time :2023/4/10 16:45
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 裁剪网格纸.py
# @Software :PyCharm

n = int(input())
list1 = []
list_x = []  # 表示x,y的坐标
list_y = []
res = 0
for i in range(n):
    list1 = list(map(int, input().split()))
    list_x.append(list1[0])
    list_y.append(list1[1])
min_x, min_y = min(list_x), min(list_y)
max_x, max_y = max(list_x), max(list_y)
res = max(max_x-min_x, max_y-min_y)**2