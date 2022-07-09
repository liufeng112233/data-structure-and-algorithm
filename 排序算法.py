import random


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


li = [random.randint(0, 10000) for i in range(10)]
print(li)
bubble_sort(li)
print(li)


def select_sort_simple(li):
    li_new = []
    for i in range(len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new


def selcet_sort(li):
    for i in range(len(li) - 1):
        min_loc = i
        for j in range(i, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]
        print(li)


li = [3, 2, 4, 1, 5, 6, 7, 9]
selcet_sort(li)


def insert_sort(li):  # 插入排序 O(n^2)
    for i in range(1, len(li)):  # 表示摸到的牌的下标
        temp = li[i]
        j = i - 1  # j表示的是手里的牌的下标
        while j >= 0 and li[j] > temp:
            li[j + 1] = li[j]
            j -= 1
            li[j + 1] = temp
            print(i)


"""
    快递排序
"""
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
        # print(li, 'right')
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]  # 把左边的值写到右边空位上
        # print(li, 'left')
    li[left] = tmp  # 把tmp归位
    return left


def quick_sort(data, left, right):
    if left < right: # 至少两个元素
        mid = partition(data, left, right)
        quick_sort(data, left, mid - 1)
        quick_sort(data.mid + 1, right)
