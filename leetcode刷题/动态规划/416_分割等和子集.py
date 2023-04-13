# -*- codeing = utf-8 -*-
# @time :2023/3/30 19:39
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 416_分割等和子集.py
# @Software :PyCharm
"""
    1、sum(nums)%2==1或len(nums)<2此时返回False
    2、sum(nums)%2==0
        数组排序，查找最大值，如果最大值大于sum/2,则不存在这两额数组划分

"""


# 二维度数组解法
class Solution:
    def canPartition(self, nums):
        target = sum(nums)
        nums = sorted(nums)

        # 做最初的判断
        if target % 2 != 0:
            return False

        # 找到 target value 可以认为这个是背包的体积
        target = target // 2

        row = len(nums)  # 行
        col = target + 1  # 列

        # 定义 dp table，主要存储每个0——target的元素组成
        dp = [[0 for _ in range(col)] for _ in range(row)]

        # 初始 dp 初始边界值target=0，此时表示分割的数组为空
        for i in range(row):
            dp[i][0] = 0

        for j in range(1, target):  # 处理第一行数组的一个元素
            if nums[0] <= j:
                dp[0][j] = nums[0]

        # 遍历 先遍历物品再遍历背包
        for i in range(1, row):  # 每个元素处理

            cur_weight = nums[i]
            cur_value = nums[i]

            for j in range(1, col):
                if cur_weight > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cur_weight] + cur_value)

        # 输出结果
        return dp[-1][col - 1] == target


y = Solution()
nums = [1, 5, 11, 5]
res = y.canPartition(nums)


class Solution:
    def canPartition(self, nums):
        n = len(nums)
        if n < 2:
            return False
        sum_nums = sum(nums)
        if sum_nums % 2 == 1:
            return False
        target = sum_nums // 2
        # 处理特诉情况，如果nums最大是大于target，不存在
        max_nums = max(nums)
        if max_nums > target:
            return False

        dp = [[False for _ in range(target + 1)] for _ in range(n)]
        # 处理target=0的边界情况，才是【0，i】之间只有一个整数可以选择
        for i in range(n):
            dp[i][0] = True

        dp[0][nums[0]] = True
        for i in range(1, n):
            num = nums[i]
            for j in range(1, target + 1):
                if j >= num:
                    dp[i][j] = dp[i - 1][j] | dp[i - 1][j - num]
                else:
                    dp[i][j] = dp[i - 1][j]
        return dp[n-1][target]
