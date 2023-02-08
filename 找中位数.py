# -*- codeing = utf-8 -*-
# @time :2022/10/4 20:23
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 找中位数.py
# @Software :PyCharm
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        # nums1全部小于num2
        if nums1[m - 1] <= nums2[0]:
            nums = nums1 + nums2
            if (m + n) % 2 != 0:
                median_value = nums[int((m + n) / 2)]
            if (m + n) % 2 == 0:
                median_value = 0.5*(nums[int((m + n ) / 2)] + nums[int((m + n -2) / 2)])
        # nums2全部小于num1
        if nums2[n-1] <= nums1[0]:
            nums = nums2 + nums1
            if (m + n) % 2 != 0:
                median_value = nums[int((m + n) / 2)]
            if (m + n) % 2 == 0:
                median_value = 0.5 * (nums[int((m + n) / 2)] + nums[int((m + n - 2) / 2)])
        #
        if nums1[0]<=nums2[0] and nums1[m-1]>=nums2[n-1]:
            if (m + n) % 2 != 0:
                print()


