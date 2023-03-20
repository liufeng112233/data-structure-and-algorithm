# -*- codeing = utf-8 -*-
# @time :2023/2/22 21:50
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 动态规划_公共子序列.py
# @Software :PyCharm
"""
    一个序列的子序列在该序列中删除若干元素后得到的序列
    字符串相似度比对
    动态规划_最长公共子序列
"""


def lec_length(x, y):
    #     A= "ABCBDAB"
    #     B="BDCABA"
    #     x=A
    #     y =B
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
            else:
                c[i][j] = max(c[i - 1][j], c[i][j - 1])
    return c[m][n]


def lcs(x, y):
    m = len(x)
    n = len(y)
    c = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    b = [[0 for _ in range(n + 1)] for _ in range(m + 1)]  # 1，左上方 2 上方 3 左方
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                c[i][j] = c[i - 1][j - 1] + 1
                b[i][j] = 1  # ←
            elif c[i - 1][j] > c[i][j - 1]:  # 来自于上方
                c[i][j] = c[i - 1][j]
                b[i][j] = 2  #↑
            else:
                c[i][j] = c[i][j - 1]
                b[i][j] = 3  # ↖
    return c[m][n], b


def lcs_trackback(x, y):
    c, b = lcs(x, y)
    i = len(x)
    j = len(y)
    res = []
    while i > 0 and j > 0:
        if b[i][j] == 1:    # 来自左上方=>匹配
            res.append(x[i-1])
            i -= 1
            j -= 1
        elif b[i][j] == 2:  # 来自于上方=>不匹配
            i -= 1
        else: # ==3 来自于左方=>不匹配
            j -= 1
    return "".join(reversed(res))

A = "ABCBDAB"
B = "BDCABA"
c, b = lcs("ABCBDAB", "BDCABA")
for _ in b :
    print()
