# -*- codeing = utf-8 -*-
# @time :2023/3/16 21:01
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 442_数组中额重复的数据.py
# @Software :PyCharm
# 采用嘻哈表的形式存贮
class Solution(object):
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = [4, 3, 2, 7, 8, 2, 3, 1]
        # nums = [1,1,2]
        dic = {}
        res = []
        for i, num in enumerate(nums):
            if num in dic:
                dic[num] += 1
                res.append(num)
            else:
                dic[num] = 1
        # for num in list(set(nums)):
        #     if dic[num] == 2:
        #         res.append(num)
        res.sort()
