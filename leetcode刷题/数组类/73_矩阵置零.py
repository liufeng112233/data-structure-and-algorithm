# -*- codeing = utf-8 -*-
# @time :2023/3/23 21:35
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 73_矩阵置零.py
# @Software :PyCharm
class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        matrix = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
        m, n = len(matrix), len(matrix[0])
        dic = []
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dic.append([i, j])
        for c in dic:
            i, j = c
            for k in range(n):  # 行
                matrix[i][k] = 0
            for k in range(m):  # 列置零
                matrix[k][j] = 0
        return matrix
