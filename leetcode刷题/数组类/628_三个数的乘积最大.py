# -*- codeing = utf-8 -*-
# @time :2023/3/18 14:36
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 628_三个数的乘积最大.py
# @Software :PyCharm
class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]   # 起码大于三
        :rtype: int
        """
        # nums = [-100, -98, -1, 2, 3, 4]
        nums.sort()
        negative = 0
        for i in range(len(nums)):   # 判断有几个负数，如果多余两个负数，那么需要考虑两个负数乘积为正数
            if nums[i] < 0:
                negative += 1
            if negative == 2:
                break
        if negative == 2:  # 出现起码两个负数，那么需要计算比较
            return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])
        else:  # 一个负数或者没有负数
            return nums[-1] * nums[-2] * nums[-3]

