# -*- codeing = utf-8 -*-
# @time :2022/10/11 21:01
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 数据结构入门.py
# @Software :PyCharm
#  题目：217——存在重复元素
class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) < len(nums)

    def otherSolution(self, nums):
        table = {}  # 字保存数据
        for num in nums:
            if num in table: return True
            table[num] = 1
        return False
