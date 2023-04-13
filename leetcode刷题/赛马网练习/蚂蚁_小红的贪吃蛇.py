# -*- codeing = utf-8 -*-
# @time :2023/4/12 20:30
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 蚂蚁_小红的贪吃蛇.py
# @Software :PyCharm
n = int(input())  # 操作步数
ops = input()  # 操作指令。列表
m = int(input())  # 食物的数量
food_pos = set()  # 控制出现重复的食物位置
for _ in range(m):
    i, j = list(map(int, input().split()))
    food_pos.add((i, j))
body_pos = [(0, 0)]  # 定义初始位置
for i in range(n):
    op = ops[i]
    if op == 'W':  # 上
        x, y = body_pos[0][0], body_pos[0][1] + 1
    elif op == 'S':  # xia
        x, y = body_pos[0][0], body_pos[0][1] - 1
    elif op == 'A':  # xia
        x, y = body_pos[0][0] - 1, body_pos[0][1]
    elif op == 'D':  # xia
        x, y = body_pos[0][0] + 1, body_pos[0][1]
    if (x, y) in body_pos[1:]:  # 判断节点是否重复，就是是否出现首位相连
        break
    # 如果吃到食物，进行坐标处理
    if (x, y) in food_pos:  # 删除食物坐标
        food_pos.remove((x, y))
    else:
        body_pos.pop(0)  # 删除前一个节点，节点更新
    body_pos.append((x, y))  # 将新节点加入
