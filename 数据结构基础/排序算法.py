# 冒泡排序
def bubble_sort(li):
    for i in range(len(li) - 1):  # 定义趟数
        exchange = False  # 添加标志位，主要是解决无序区也自然有序的情况[9,8,7,1,2,4,5,6]
        for j in range(len(li) - i - 1):
            if li[j] < li[j + 1]:  # 降序<，升序>
                li[j], li[j + 1] = li[j + 1], li[j]  # 两个数交换位置
                exchange = True
        if not exchange:
            return

# 冒泡排序主要注意无序区的关系
def maopao_sort(li):
    L = len(li)
    for i in range(L - 1):
        changge = False
        for j in range(L - i - 1):
            if li[j + 1] < li[j]:
                li[j], li[j + 1] = li[j + 1], li[j]
                changge = True   # 表示不再进入该循环，后面的数据自然成组
        if not changge:
            return

import random

li = [random.randint(0, 10000) for i in range(10)]
print(li)
maopao_sort(li)
print(li)
#
#
# # 选择排序
def select_sort_simple(li):
    li_new = []
    for i in range(len(li)):
        min_val = min(li)   # 选择最小值
        li_new.append(min_val)  # 进行栈添加
        li.remove(min_val)   # 采用内置函数去除已经有序数值
    return li_new
#
#
def selcet_sort(li,len1):
    for i in range(len1-1):
        min_loc = i
        for j in range(i+1, len1):
            if li[j] > li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]
        print(li)
#
#
li = [1,2,4,3]
selcet_sort(li,2)
#
#
def insert_sort(li):  # 插入排序 O(n^2)
    for i in range(1, len(li)):  # i提取的是无序区的数据
        temp = li[i]
        j = i - 1
        while j > -1 and temp < li[j]:  # j表示有序去数字5
            li[j + 1] = li[j]  # 有序区数据移动，直到可以放下无序区的丢一个数据位置
            j = j - 1  # 直到有序去区的数据全部对比完成
        li[j + 1] = temp
        print(li)


#### 折半排序：不使用嵌套函数，直接采用函数封装API的方式
def insert_half_sort(li):
    length = len(li)
    print(li)
    for i in range(1, length):
        waitting_insert_key = li[i]
        low, high = 0, i - 1
        while low <= high:  # 这里是折半排序的序号处理方式
            mid = (low + high) // 2
            if li[mid] > waitting_insert_key:  # 中间数值还在low的一边
                high = mid - 1
            else:
                low = mid + 1
        j = i - 1
        while j >= high + 1:
            li[j + 1] = li[j]
            j = j - 1
        li[high + 1] = waitting_insert_key
        print(li)
#
#
# """
#     快速排序
# """
#
#
def partition(li, left, right):
    '''

    :param li: 列表
    :param left: 列表左侧值下标
    :param right: 列表右侧值下标
    :return:
    '''
    tmp = li[left]
    while left < right:
        while left < right and li[right] >= tmp:  # 从右面找比tmp小的数
            right -= 1  # 往左走一步
        li[left] = li[right]  # 把右边的值写到左边空位上
        print(li, 'right')
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]  # 把左边的值写到右边空位上
        print(li, 'left')
    li[left] = tmp  # 把tmp归位
    print("最终结果   {}".format(li))
    return left
#
#
def quick_sort(data, left, right):
    if left < right:  # 至少两个元素
        mid = partition(data, left, right)
        print("划分子列表  {}".format(data))
        quick_sort(data, left, mid - 1)
        print("左侧列表  {}".format(data))
        quick_sort(data, mid + 1, right)
        print("右侧列表  {}".format(data))
#
#
# li = [5, 7, 4, 6, 3, 1, 2, 9, 8, 10]
# partition(li, 0, len(li) - 1)
# quick_sort(li, 0, len(li) - 1)
# import copy
#
#
# 归并排序
def merge(li, low, mid, high):
    i = low
    j = mid + 1
    ltmp = []
    while i <= mid and j <= high:  # 只要两边都有数
        if li[i] < li[j]:
            ltmp.append(li[i])
            i += 1
        else:
            ltmp.append(li[j])
            j += 1
    # while执行完成，肯定有一部分没数了
    while i <= mid:
        ltmp.append(li[i])
        i += 1
    while j <= high:
        ltmp.append(li[j])
        j += 1
        li[low:high + 1] = ltmp
#
#
# # 中间两部分数假定有序的
# li = [2, 4, 5, 7, 1, 3, 6, 8]
# merge(li, 0, 3, 7)
# print(li)
#

"""
    希尔排序算法
"""
def insert_sort_gap(li, gap):
    # gap 分组数
    for i in range(gap, len(li)):  # i 表示摸到的牌的下标
        tmp = li[i]
        j = i - gap  # j表示手里牌的下标
        while j >= 0 and li[j] > tmp:
            li[j + gap] = li[j]
            j -= gap
        li[j + gap] = tmp

def shell_sort(li):
    d = len(li) // 2
    while d >= 1:
        insert_sort_gap(li, d)
        d //= 2
#
# # 测试
# li = list(range(100))
# import random
# random.shuffle(li)
# shell_sort(li)
# print(li)

"""
    计数排序
"""


def count_sort(li, max_count=100):
    count = [0 for i in range(max_count + 1)]
    for val in li:
        count[val] += 1
    li.clear()
    for ind, val in enumerate(count):
        for j in range(val):
            li.append(ind)


import random

li = [random.randint(0, 100) for _ in range(1000)]
print(li)
count_sort(li)
print(li)

"""" 
    桶排序
"""


def bucket_sort(li, n=100, max_num=10000):
    """
    :param li:  需要处理的列表
    :param n: 桶的数量
    :param max_num:  列表中的最大数值
    :return: 返回列表
    """
    buckets = [[] for _ in range(n)]  # 创建列表作为桶，每个桶100个数，依次递增
    for var in li:
        i = min(var // (max_num // n), n - 1)  # i表示var值放到哪个桶中间,每个桶方max_num//n个数，其实就是10000的值放缩到100之间
        buckets[i].append(var)
        # 直接桶里面排序，冒泡排序、插入排序
        for j in range(len(buckets[i]) - 1, 0, -1):
            if buckets[i][j] < buckets[i][j - 1]:
                buckets[i][j], buckets[i][j - 1] = buckets[i][j - 1], buckets[i][j]
            else:
                break
    sorted_li = []
    for buc in buckets:
        sorted_li.extend(buc)
    return sorted_li


import random

li = [random.randint(0, 10000) for _ in range(100000)]
# print(li)
li = bucket_sort(li)
print(li)
"""
    基数排序：多关键字排序，比如年龄、在按照薪资排序
"""


# 一直都是循环处理。依次先按照个位、十位依次排序，每次处理钱都是重新定义的列表，复杂度O(kn)
def radix_sort(li):
    max_num = max(li)  # 最大值维数确定循环次数
    it = 0
    while 10 ** it <= max_num:   # K表示循环的次数
        buckets = [[] for _ in range(10)]
        for var in li:
            digit = (var // 10 ** it) % 10
            buckets[digit].append(var)
            # print(var)
        # 分桶
        li.clear()
        for buc in buckets:
            li.extend(buc)
        # 把数重新放回li
        it += 1


import random
import numpy as np

li = list(range(1000))
random.shuffle(li)
li2 = np.array(li)
radix_sort(li)
print(li)

# 技术排序按照关键字排序