# -*- codeing = utf-8 -*-
# @time :2023/3/8 9:11
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 双指针——最大水桶问题.py
# @Software :PyCharm

# 方法一
class Solution:
    def maxArea(self, height):
        self.left = 0
        self.right = len(height) - 1
        self.result = 0
        while self.left < self.right:
            if height[self.left] < height[self.right]:
                self.result = max(self.result, height[self.left] * (self.right - self.left))
                self.left += 1
            else:
                self.result = max(self.result, height[self.right] * (self.right - self.left))
                self.right -= 1
        return self.result


# 方法二
"""
    在双指针交替移动过程中，还可以进一步剔除不可能构成最大值的边;
    以右指针为例，在右指针左移过程中，任何在当前指针左边且高度低于当前指针所指边的高度的边都不可能构成最大值。
    因为该边相较于当前指针所指边宽度变窄，高度变低，因此不能构成最大值
    [1,8,6,2,5,4,8,3,7]----->2,3,4,5,7号边低于8号，因此2,3,4,5,7在右指针左移过程中可以直接跳过。由此进一步优化指针移动代码可得
"""


class Solution:
    def maxAera(self, height):
        # 记录左边、右边指针所经历的最大高度
        maxleft = -1
        maxright = -1
        maxV = -1  # 最大值
        # 左右指针
        left = 0
        right = len(height) - 1
        # 中间体积变量
        V = 0
        while left < right:
            V = (right - left) * min(height[left], height[right])  # 体积又最小板决定
            if V > maxV:
                maxV = V
            # 移动左指针
            if height[left] < height[right]:
                while height[left] <= maxleft and left < right:
                    left += 1
                maxleft = height[left]
            # 移动右指针
            else:
                while height[right] <= maxright and left < right:
                    right -= 1
                maxright = height[right]
        return maxV
