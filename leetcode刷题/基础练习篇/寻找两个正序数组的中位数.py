# -*- codeing = utf-8 -*-
# @time :2023/2/18 13:19
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 寻找两个正序数组的中位数.py
# @Software :PyCharm

class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        self.num = nums2 + nums1
        # 折半排序
        self.length = len(self.num)
        for i in range(1, self.length):
            waitting_insert_key = self.num[i]  # 暂存数值
            low, high = 0, i - 1
            while low <= high:  # 这里是折半排序的序号处理方式
                mid = (low + high) // 2
                if self.num[mid] > waitting_insert_key:  # 中间数值还在low的一边
                    high = mid - 1
                else:
                    low = mid + 1
            j = i - 1
            while j >= high + 1:
                self.num[j + 1] = self.num[j]
                j = j - 1
            self.num[high + 1] = waitting_insert_key
        if self.length % 2 == 1:  # 奇数个数
            return self.num[(self.length - 1) // 2]
        elif self.length % 2 == 0:  # 偶数
            # 输出是小数时，其中除数应该是2.0 而不是2
            return (self.num[(self.length - 1) // 2] + self.num[(self.length + 1) // 2]) / 2.0
