# -*- codeing = utf-8 -*-
# @time :2023/3/15 21:10
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 645_错误的数组.py
# @Software :PyCharm
class Solution(object):
    def findErrorNums(self, nums):
        """
        :type :
        :rtype:
        """
        s = sum(set(nums))
        n = sum(nums)
        c = 0
        for i in range(1, len(nums) + 1):
            c += i
        return [n - s, c - s]


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type :
        :rtype:
        """
        n = len(nums)
        nums.sort()
        lose = -1
        repeat = -1
        if nums[0] != 1:
            lose = 1
        elif nums[-1] != n:
            lose = n
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                repeat = nums[i]
            if nums[i] - nums[i - 1] == 2:  # 两个数之间的插值为2是中间必须缺少一个值
                lose = nums[i] - 1
        return [repeat, lose]


class Solution(object):
    def findErrorNums(self, nums):
        """
        :type :
        :rtype:
        """
        n = len(nums)
        repeat = 0  # jilu
        lose = 0
        for i in range(n):
            if nums.count(nums[i]) == 2:  # 统计重复数据的数量
                repeat = nums[i]
            if nums.count(i + 1) == 0:
                print(nums.count(i + 1))
                lose = i + 1
        return [repeat, lose]


y = Solution()
nums = [2, 2]
# nums.count(2)
# re = y.findErrorNums(nums)
