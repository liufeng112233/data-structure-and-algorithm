# -*- codeing = utf-8 -*-
# @time :2023/3/18 9:32
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 414_第三大的数.py
# @Software :PyCharm
class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # nums = [-1,2,3]
        nums = list(set(nums))   # 先set后面在采用随机随机嘻哈表实现，所以会存在改变顺序
        nums.sort()  # 所以先去除重复值在排序，放前面会出现案例不通过
        if len(nums) < 3:
            return nums[-1]
        else:
            del nums[-1]
            del nums[-1]
            return nums[-1]
