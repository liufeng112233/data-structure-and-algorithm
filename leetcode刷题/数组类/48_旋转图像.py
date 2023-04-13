# -*- codeing = utf-8 -*-
# @time :2023/3/23 20:31
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 48_旋转图像.py
# @Software :PyCharm
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        # matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
        n = len(matrix)
        # 通过计算规律
        # matrix_new[j][3-i] = matrix[i][j]
        matrix_new = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                matrix_new[j][n - i - 1] = matrix[i][j]
        # 这里应该是引用拷贝
        matrix[:] = matrix_new
        return matrix


class Solution1():
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            for j in range(len(matrix)//2):
                matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]
        return matrix
matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
y = Solution1()
res = y.rotate(matrix)