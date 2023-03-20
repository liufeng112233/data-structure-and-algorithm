# -*- codeing = utf-8 -*-
# @time :2023/3/14 21:21
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 189_旋转数组.py
# @Software :PyCharm
class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        """
            1、需要判断循环多个周期,周期循环不改变顺序，所以处理余数：kk=k%len(nums)
            2、判断循环数据是否有效，符合题意的问题
            3、栈保存数据，采用（n-k-1，n-1）输出进栈，后面在（0，n-k-1）进栈
        """
        stack = []
        l = len(nums)
        kk = k % l
        for i in range(l - kk, l):
            stack.append(nums[i])
        for j in range(0, l - kk):
            stack.append(nums[j])
        nums = stack


class Solution:
    def rotate(self, nums, k):
        new_nums = nums + nums  # 这个可以解决O(1)的问题
        kk = k % len(nums)  # 剔除周期性问题
        for i in range(len(nums)):
            nums[i] = new_nums[i + len(nums) - kk]  # 这里就是选择相对应的数据就行

class Solution:
    def rotate(self,nums,k):
        # 采用反转数组的方式进行
        nums = [1,2,3,4,5,6,7]
        kk  = k%len(nums)
        if kk!=0:
            list.reverse(nums)
            nums1 = nums[0:kk]
            nums2 = nums[kk:]
            list.reverse(nums1)
            list.reverse(nums2)
            nums[0:kk]= nums1
            nums[kk:] = nums2

