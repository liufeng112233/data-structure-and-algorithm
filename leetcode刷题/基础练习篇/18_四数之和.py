# -*- codeing = utf-8 -*-
# @time :2023/3/10 20:22
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 18_四数之和.py
# @Software :PyCharm
class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums = self.select_sort(nums)
        res = []
        if len(nums) < 4:
            return res
        for i in range(len(nums)):  # 前面三个值
            # if nums[i] > target:
            #     break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums)):
                # if nums[j] > target-nums[i]:
                #     break
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, len(nums) - 1
                while left < right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if sum == target:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
                    elif sum < target:
                        left += 1
                    elif sum > target:
                        right -= 1
        return res

    # 插入排序，移动数据
    def select_sort(self, li):
        for i in range(len(li)):
            temp = li[i]
            j = i - 1
            while j > -1 and temp < li[j]:
                li[j + 1] = li[j]
                j = j - 1
            li[j + 1] = temp
        return li
