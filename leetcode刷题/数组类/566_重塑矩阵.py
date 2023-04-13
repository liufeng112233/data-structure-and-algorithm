# -*- codeing = utf-8 -*-
# @time :2023/3/23 19:48
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 566_重塑矩阵.py
# @Software :PyCharm
class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        # mat = [[1, 2,3,4], [5, 6,7,8]]
        # r = 1
        # c = 8
        k, m, n = 0, len(mat), len(mat[0])  # 定义新数组的在第几行放数据和矩阵边界
        res = [[] for _ in range(r)]   # 根据需要转存的胡
        if m * n != r * c:   # 判断是否满足转存条件
            return mat
        else:
            for i in range(m):
                for j in range(n):   # 正常全序遍历
                    res[k].append(mat[i][j])   # 数据
                    if len(res[k]) == c:   # 当列满足条件时进入下一行
                        k += 1
        return res