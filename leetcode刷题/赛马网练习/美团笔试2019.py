# -*- codeing = utf-8 -*-
# @time :2023/4/4 20:12
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 美团笔试2019.py
# @Software :PyCharm
import sys

n = int(input())
list2 = []
for i in range(n):
    list2.append(list(map(int, input().split())))
# 现在输入是对的 [[1, 5], [2, 4], [2, 3], [1, 4], [2, 5]]
l = len(list2)
total = 0
j = 0
i = l - 1
left, right = 1000000, 0
while i > 0:
    left, right = list2[i][0], list2[i][1]
    j = i - 1
    while left <= list2[j][0] and right >= list2[j][1]:
        total += 1
        j -= 1
        i = j
    else:
        i=j
print(total)
