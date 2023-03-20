# -*- codeing = utf-8 -*-
# @time :2023/2/15 21:03
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 列表数据拼接.py
# @Software :PyCharm
class Solution(object):
    def findTheArrayConcVal(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        L = len(nums)
        data = 0
        left = 0
        right = L - 1
        while left < right:
            data_r = str(nums[right])
            data_l = str(nums[left])
            data_tmp = int(data_l + data_r)
            data = data + data_tmp
            left += 1
            right -= 1
            if left ==right:
                data = data+nums[left]
        return data
nums1 = [7,52,2,4]
nums2 = [5,14,13,8,12]
data1 = Solution.findTheArrayConcVal(nums=nums1)