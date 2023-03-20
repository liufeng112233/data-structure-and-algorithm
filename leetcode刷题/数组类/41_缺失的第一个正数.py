# -*- codeing = utf-8 -*-
# @time :2023/3/17 16:01
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 41_缺失的第一个正数.py
# @Software :PyCharm
# 如果没有时间复杂度直接嘻哈表存储数据，通过循环对比直接各处最小值
# 利用符号构建嘻哈函数

class Solution:
    def firstMissingPositive(self, nums):
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0:
                nums[i] = n + 1

        for i in range(n):  # 此时的数据全部是正数，对于负数前面处理后大于N，下面运算后保持不变
            num = abs(nums[i])    # 寻找对应的序号，说明存在，不存在的就不会有标签
            if num <= n:
                nums[num - 1] = -abs(nums[num - 1])  # 其中符号表示该位置的数据有了

        for i in range(n):
            if nums[i] > 0:  # 表示该位置数据缺失
                return i + 1
        return n + 1


# 方法二，自制嘻哈函数，通过数据的交换进行将数据放到正确位置
class Solution:
    def firstMissingPositive(self, nums):  # 自制嘻哈表，利用负数作为响应稀疏
        size = len(nums)
        for i in range(size):
            # 判断数据是不是索引i,判断这个数是不是放大正确的位置，依据数组的数据作为主导进行好考虑
            while i <= nums[i] <= size and i != (nums[i] - 1):  # 其实负数对于我数据的移动并没有影响
                self.exchange(nums, i, nums[i] - 1)  # 交换相应数值
        for i in range(size):  # 正常的遍历
            if i + 1 != nums[i]:  # 当第一次满足该函数时直接跳出函数
                return i + 1

    def exchange(self, nums, index1, index2):
        nums[index1], nums[index2] = nums[index2], nums[index1]


nums = [3, 4, -1, 1]
y = Solution()
res = y.firstMissingPositive(nums)
