# -*- codeing = utf-8 -*-
# @time :2023/3/24 21:17
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 303_区域和检索-数组不可变.py
# @Software :PyCharm

class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums


    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        sum_total = sum(self.nums[left:right+1])
        return sum_total



# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


# -*- codeing = utf-8 -*-
# @time :2023/3/24 21:17
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 303_区域和检索-数组不可变.py
# @Software :PyCharm

class NumArray(object):   # 空间换时间

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.sum_nums = [0]
        for i in range(len(self.nums)):  # 表示计算前i元素的和并存处下来，两个数之间的插值就是right-left
            self.sum_nums.append(self.sum_nums[-1]+self.nums[i])



    def sumRange(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: int
        """
        sum_total = self.sum_nums[right+1]-self.sum_nums[left]
        return sum_total



