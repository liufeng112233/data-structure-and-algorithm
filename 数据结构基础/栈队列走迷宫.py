# -*- codeing = utf-8 -*-
# @time :2023/2/13 9:21
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 栈队列走迷宫.py
# @Software :PyCharm
#! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 24/12/2017

# maze = [
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#     [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
#     [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
#     [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
#     [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
#     [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
#     [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
#     [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
#     [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
#     [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
# ]
# # x，y四个方向，（x+1,y）,(x-1,y),(x,y-1),(x,y+1)
# dirs = [
#     lambda x,y: (x+1,y),
#     lambda x,y: (x-1,y),
#     lambda x,y: (x,y-1),
#     lambda x,y: (x,y+1)
# ]
#
# def maze_path(x1,y1,x2,y2):
#     stack = []
#     stack.append((x1, y1))  # 存的是元组
#     while(len(stack)>0):  # 栈空表示没有通路
#         curNode = stack[-1] # 当前的节点
#         # 判断当前节点的是否是终点
#         if curNode[0] == x2 and curNode[1] == y2:
#             # 走到终点了
#             for p in stack:
#                 print(p)
#             return True
#
#         # x,y 四个方向 x-1,y; x+1,y; x,y-1; x,y+1
#         for dir in dirs:
#             nextNode = dir(curNode[0], curNode[1])
#             # 如果下一个节点能走
#             if maze[nextNode[0]][nextNode[1]] == 0:
#                 stack.append(nextNode)
#                 maze[nextNode[0]][nextNode[1]] = 2 # 2表示为已经走过
#                 break
#         else:
#             maze[nextNode[0]][nextNode[1]] = 2
#             stack.pop()
#     else:
#         print("没有路")
#         return False
#
# maze_path(1,1,8,8)

"""
    队列激进行迷宫问题
    第一列出队写
"""
from collections import deque    #创建队列

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

dirs = [
    lambda x, y: (x + 1, y),
    lambda x, y: (x - 1, y),
    lambda x, y: (x, y - 1),
    lambda x, y: (x, y + 1)
]


def print_r(path):
    curNode = path[-1]

    realpath = []

    while curNode[2] == -1:
        realpath.append(curNode[0:2])
        curNode = path[curNode[2]]

    realpath.append(curNode[0:2])  # 起点
    realpath.reverse()
    for node in realpath:
        print(node)


def maze_path_queue(x1, y1, x2, y2):
    queue = deque()
    queue.append((x1, y1, -1))   # 位置及队列表示序号
    path = []
    while len(queue) > 0:
        curNode = queue.pop()  # 出队
        path.append(curNode)
        if curNode[0] == x2 and curNode[1] == y2:
            # 终点
            print_r(path)
            return True
        for dir in dirs:
            nextNode = dir(curNode[0], curNode[1])
            if maze[nextNode[0]][nextNode[1]] == 0:
                queue.append((nextNode[0], nextNode[1], len(path) - 1))  # 后续节点进队，记录哪个节点带他来的
                maze[nextNode[0]][nextNode[1]] = 2  # 标记为已经走过
    else:
        print("没有路")
        return False


maze_path_queue(1, 1, 8, 8)

