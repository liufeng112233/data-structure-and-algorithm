# -*- codeing = utf-8 -*-
# @time :2023/4/10 17:22
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : BD3钓鱼比赛.py
# @Software :PyCharm
import sys

# round 函数可以进机型格式化，round(x,2),2表示几位小数
# 至少一条的对立事件就是一条鱼都没有钓到
while True:
    try:
        n, m, x, y, t = [int(i) for i in input().split()]
        arr = []
        prob_sum = 0  # 保存总的概率
        for i in range(n):
            arr.append(list(map(float, input().strip().split())))
            prob_sum += sum(arr[-1])
        # 对于cc，（x,y）
        cc = arr[x - 1][y - 1]
        cc_win = 1 - (1 - cc) ** t
        # 对 yy每格得平均概率
        ss = prob_sum / (n * m)
        ss_win = 1 - (1 - ss) ** t
        if cc == ss:
            print("epual")
            print("%.2f" % cc)
        elif cc>ss:
            print("cc")
            print("%.2f" % cc_win)
        elif cc<ss:
            print("ss")
            print("%.2f" % ss_win)
    except:
        break
