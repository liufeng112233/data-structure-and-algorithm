# -*- codeing = utf-8 -*-
# @time :2023/4/5 9:32
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 排序算法_汇总.py
# @Software :PyCharm
"""
    1、二分查找
"""
def binary_search(nums, val):
    # 首先需要原始数据值需要有序的
    nums.sort()
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2  # 必须取整

        if nums[mid] > val:
            right = mid - 1
        elif nums[mid] < val:
            left = mid + 1
        else:
            return mid
    else:
        return None


nums = [1, 8, 7, 9, 3, 4, 2, 5, 6]


# 选择排序
def select_sort(nums):
    for i in range(len(nums) - 1):  # 为后面的无序区至少预留一个位置，不然后面报错
        temp = i  # 暂存边界
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[temp]:
                temp = j  # 暂存后面无序区的最小值位置
        nums[i], nums[temp] = nums[temp], nums[i]  # 是的i此时是后面的最小值


# 插入排序
def insert_sort(nums):
    for i in range(1, len(nums)):
        temp = nums[i]   # 暂存器有序无序对比值，方面插入是通过移动数组，所只需要暂存一个边界变量
        j = i - 1
        while j > -1 and temp < nums[j]:
            nums[j + 1] = nums[j]  # 挨个对比移动
            j -= 1   # 直到有序区的数据全部对比完成
        nums[j + 1] = temp

