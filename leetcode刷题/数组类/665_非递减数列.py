# -*- codeing = utf-8 -*-
# @time :2023/3/14 17:32
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 665_非递减数列.py
# @Software :PyCharm

"""
    给你一个长度为 n 的整数数组 nums ，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。
我们是这样定义一个非递减数列的： 对于数组中任意的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。
"""

"""
    给你一个长度为 n 的整数数组 nums ，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。
我们是这样定义一个非递减数列的： 对于数组中任意的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。
"""


class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # 进来标志位，记录i>i+1的个数，如果个数大于1则直接输出false
        dic = {}
        flag = 0  # 标志位
        for i in range(1, len(nums)):
            if nums[i - 1] > nums[i]:   # 只有当其大于后面一个数是才判断三个数并赋值
                flag += 1
                if i == 1 or nums[i] >= nums[i - 2]:   # 此时中间数一要满足递增的条件，那么需要改变那就是幅值后面i的值，使得相邻相等
                    nums[i - 1] = nums[i]
                else:
                    nums[i] = nums[i - 1]    # 此时i-1位置的数据是满足条件的
            elif flag > 1:
                break
        if flag <= 1:
            return True
        else:
            return False


# nums = [4, 2, 3, 4, 5]
nums = [3, 4, 2, 5]


y = Solution()
res = y.checkPossibility(nums)
