# -*- codeing = utf-8 -*-
# @time :2022/10/26 19:49
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 希尔排序.py
# @Software :PyCharm
def insert_sort_gap(li, gap):
    for i in range(gap, len(li)):
        temp = li[i]
        j = i - gap
        while j >= 0 and li[j] > temp:
            li[j + gap] = li[j]
        li[j + gap] = temp


def shell_sort(li):
    d = len(li) // 2
    while d >= 1:
        insert_sort_gap(li, d)
        d //= 2


li=list(range(1000))
import random
random.shuffle(li)
shell_sort(li)
print(li)