class Solution:
    def minMoves(self, nums):
        min_num = min(nums)  # 存储最小值
        res = 0
        for num in nums:
            res += num - min_num   # 两个数之间的操作步骤
        return res


