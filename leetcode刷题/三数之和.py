# -*- codeing = utf-8 -*-
# @time :2023/3/9 9:32
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 三数之和.py
# @Software :PyCharm
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        '''
            (1)对数组进行排序，判断num[0] 和len(num)是否满足一个组合3元素
            (2)确定第一个数，后面的两个数采用双指针从（i+1）开支left和right向中间汇合
            （3）当left<right时。计算sum = num[i]+num[left]+num[right]
                1)判断num[i]>0,后面的数均不满足求和，直接跳出break
                2）判断第一个数是否重复，num[i]=num[i-1]重复，直接跳过该次循环，直接进入循环continue
                3）
                    (a)判断sum==0时，判断左右指针是否重复
                        left，重复left+=1
                        right，重复right-=1
                    (b)sum<0,左边数大left+=1
                    (c)sum>0,右边数大right-=1
                    
        '''
        # 排序
        res = []
        nums_new = self.selct_sort(nums)
        if nums_new[0] > 0 or len(nums) <= 2:
            return res
        for i in range(len(nums)):
            if nums_new[i] > 0:
                break # 直接代码停止，直接跳出大循环
            elif i > 0 and nums_new[i] == nums_new[i - 1]:
                continue  # 直接跳出该次循环，进入下次循环
            left, right = i + 1, len(nums) - 1
            while left < right:
                sum = nums_new[i] + nums_new[left] + nums_new[right]
                if sum == 0:
                    res.append([nums_new[i], nums_new[left], nums_new[right]])
                    while left < right and nums_new[left] == nums_new[left + 1]:
                        left += 1
                    while left < right and nums_new[right] == nums_new[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
        return res

    # 选择排序
    def selct_sort(self, li):
        for i in range(len(li)):
            min = i
            for j in range(i + 1, len(li)):
                if li[min] > li[j]:
                    min = j
            # 小数放前面
            li[i], li[min] = li[min], li[i]
        return li
