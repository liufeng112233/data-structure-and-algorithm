# -*- codeing = utf-8 -*-
# @time :2023/3/27 19:36
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 31_下一个排序.py
# @Software :PyCharm
class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # 计算标志位
        def reverse1(nums, i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1

        firstIndex = -1
        n = len(nums)
        for i in range(n - 2, -1, -1):
            if nums[i] < nums[i + 1]:  # 倒序遍历寻找第一个不是降序的数
                firstIndex = i  # 第一大数的下标
                break
        if firstIndex == -1:   # 表示整个数组都是降序排列
            reverse1(nums, 0, n - 1)
            return
        seconfindex = -1  # 在i——n-1之间的弊比nums[i]大的第一个值，就是刚好大一点点
        for i in range(n - 1, firstIndex, -1):
            if nums[i] > nums[firstIndex]:
                seconfindex = i
                break
        # 交换两个值然后再将后面降序的数值变成升序就是后面的最小值。
        nums[firstIndex], nums[seconfindex] = nums[seconfindex], nums[firstIndex]
        reverse1(nums, firstIndex + 1, n - 1)
        return
