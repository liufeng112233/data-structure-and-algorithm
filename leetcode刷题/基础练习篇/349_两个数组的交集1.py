# -*- codeing = utf-8 -*-
# @time :2023/3/14 9:46
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 349_两个数组的交集1.py
# @Software :PyCharm
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        num = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    num.append(nums1[i])
        num = set(num)


nums1 = [1, 2, 2, 1]
nums2 = [2, 2]


nums1 = [4,9,5]
nums2 = [9,4,9,8,4]