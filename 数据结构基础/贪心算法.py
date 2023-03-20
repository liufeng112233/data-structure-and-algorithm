# -*- codeing = utf-8 -*-
# @time :2023/2/21 11:00
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 贪心算法.py
# @Software :PyCharm
"""
    找零问题
"""
t = [100, 50, 20, 5, 1]


def change(t, n):
    m = [0 for _ in range(len(t))]
    for i, money in enumerate(t):
        m[i] = n // money
        n = n % money
    return m, n


print(change(t, 376))

"""
    背包问题：0-1背包，分数背包
"""
# 分数背包算法
goods = [(60, 10), (100, 20), (120, 30)]  # 元组是商品价格和重量


def fractional_backpack(goods, w):
    goods.sort(key=lambda x: x[0] / x[1], reverse=True)
    m = [0 for _ in range(len(goods))]
    for i, (prize, weight) in enumerate(goods):
        if w >= weight:
            m[i] = 1
            w -= weight
        else:
            m[i] = w / weight
            w = 0
            break
    return m


print(fractional_backpack(goods, 50))

"""
    拼接最大数问题
    同串长度、不同长度，不同长度且是子串
    可直接将两个字符串相连直接比较大小：a,b变成a+b 
"""
li = [32, 94, 128, 1286, 6, 71]

# 方法1
from functools import cmp_to_key


def xy_cmp(x, y):
    if x + y < y + x:
        return 1
    elif x + y > y + x:
        return -1
    else:
        return 0


def number_join(li):
    li = list(map(str, li))  # 将每个元素变成字符串
    # 采用加法进行排序
    li.sort(key=cmp_to_key(xy_cmp))  # 这可采用一般的排序算法即可实现x+y和判断
    return "".join(li)


# 方法2
def number_join2(li):
    li = list(map(str, li))
    # 采用x+Y的方式进行排序，这里的算法由各种排序算法
    for i in range(len(li) - 1):
        change = False
        for j in range(len(li) - i - 1):
            if int(li[j] + li[j + 1]) < int(li[j + 1] + li[j]):
                li[j], li[j + 1] = li[j + 1], li[j]
                change = True
            while not change:
                return "".join(li)
    return int("".join(li))


print(number_join2(li))

"""
    活动选择问题：
        开始时间、结束时间
        使得该场地的举办的活动个数最多
        贪心条件：
            最先结束的活动一定是最优解的一部分
"""
activities = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)]
# 保证活动是按照结束时间排好序的
activities.sort(key=lambda x: x[1])


def activity_selection(a):
    res = [a[0]]
    for i in range(1, len(a)):
        if a[i][0] >= res[-1][1]:  # 当前活动的开始时间小于等于最后一个入选的活动的结束时间
            # 不冲突
            res.append(a[i])
    return res


print(activity_selection(activities))
