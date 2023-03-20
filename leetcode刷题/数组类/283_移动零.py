# -*- codeing = utf-8 -*-
# @time :2023/3/14 20:54
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 283_移动零.py
# @Software :PyCharm
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        """"
            1、构建两个栈保存数据，
                stack1：:原始的非零数据
                Stack2：保存零数据，反向输出就原始零的相对位置数据
        """
        stack1 = []
        stack2 = []
        for c in nums:
            if c == 0:
                stack2.append(c)
            else:
                stack1.append(c)
        for c in stack2:
            stack1.append(c)
        return list(stack1)


nums = [0, 1, 0, 3, 12]
y = Solution()
res = y.moveZeroes(nums)


# 采用双指针
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        left = 0        # 指示非零数据的右端
        right = 0  # 寻找非零数据
        while right < len(nums):
            if nums[right] != 0:   # 当寻找到非零数据时，left右移一位，right和left进行交换(非零数据和；零数据的交换)
                nums[left], nums[right] = nums[right], nums[left]
                left +=1
            right+=1
        return nums

