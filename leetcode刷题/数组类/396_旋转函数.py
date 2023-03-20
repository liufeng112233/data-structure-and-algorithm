# -*- codeing = utf-8 -*-
# @time :2023/3/14 22:16
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 396_旋转函数.py
# @Software :PyCharm
class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type :
        :rtype:
        """
        max_data = []
        for _ in range(len(nums)):
            nums, data = self.RotateFunction(nums, 1)
            max_data.append(data)
        max1 = max(max_data)
        return max1

    def RotateFunction(self, nums, k):
        stack = []
        data = 0
        l = len(nums)
        kk = k % l
        for i in range(l - kk, l):
            stack.append(nums[i])
        for j in range(0, l - kk):
            stack.append(nums[j])
        for i in range(len(stack)):
            data += i * stack[i]
        return stack, data


class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type :
        :rtype:
        """
        f_0 = 0
        F_max = []
        for i, data in enumerate(nums):
            f_0 += i * data
        res = f_0
        for k in range(len(nums)):
            temp = self.RotateFunction(nums, k, f_0)
            if res < temp:
                res = temp
            f_0 = temp

        return res

    def RotateFunction(self, num, k, f_k_1):
        fk = f_k_1 + sum(num) - len(num) * num[len(num) - k - 1]
        return fk


# 上面空间复杂度小但是时间复杂度大
class Solution(object):
    def maxRotateFunction(self, nums):
        """
        :type :
        :rtype:
        """
        f, n, sum_num = 0, len(nums), sum(nums)
        for i, num in enumerate(nums):
            f += i * num
        res = f
        for j in range(n - 1, 0, -1):   # 倒序是方便处理nums[i-k]
            f = f + sum_num - n * nums[j]
            res = max(res, f)
        return res
