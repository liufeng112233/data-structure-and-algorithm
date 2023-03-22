# -*- codeing = utf-8 -*-
# @time :2023/3/20 21:14
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 54_螺栓矩阵.py
# @Software :PyCharm
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        ans = []
        if not matrix:
            return ans
        up, down, left, right = 0, len(matrix) - 1, 0, len(matrix[0]) - 1
        while True:
            for i in range(left, right + 1):  # 上层：左到右
                ans.append(matrix[left][i])
            up += 1  # 上边界加1
            if up > down:
                break
            for i in range(up, down + 1):
                ans.append(matrix[i][right])  # 右边：上到下
            right -= 1  # 右边界减1
            if right < left:
                break
            for i in range(right, left - 1, -1):  # 下层：右到左
                ans.append(matrix[down][i])
            down -= 1  # 下边界减1
            if down < up:
                break
            for i in range(down, up - 1, -1):  # 左边：下到上
                ans.append(matrix[i][left])
            left += 1  # 左边界加1
            if left > right:
                break
        return ans
