# -*- codeing = utf-8 -*-
# @time :2023/3/9 10:55
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 最接近的三数之和.py
# @Software :PyCharm
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        """
            数据排序，采用三数之和的求解方式；或者计算其最大纸盒最小值至今进行扩展关系
        """

        nums = self.select_sort(nums)  # 排序

        res = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 1):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if abs(sum - target) < abs(res - target):
                    res = sum
                if sum > target:
                    right -= 1
                else:  # 这里包含了等于的小于的情况
                    left += 1
        return res


    def select_sort(self, li):
        for i in range(len(li) - 1):
            change = False
            for j in range(len(li) - i - 1):
                if li[j] > li[j + 1]:
                    li[j], li[j + 1] = li[j + 1], li[j]
                    change = True
            if not change:
                break
        return li
