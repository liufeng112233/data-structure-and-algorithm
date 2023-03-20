# -*- codeing = utf-8 -*-
# @time :2023/3/18 15:21
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 118_杨辉三角.py
# @Software :PyCharm
class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret = list()  # 二位数组
        for i in range(numRows):  # 层数
            row = list()  # 每一层从计数
            for j in range(i + 1):  # 有多少个数
                if j == 0 or j == i:  # 处理两边的边界问题
                    row.append(1)
                else:
                    row.append(ret[i - 1][j-1] + ret[i - 1][j])   # 下一个数是上两个数的和
            ret.append(row)   # 存储矩阵
        return ret
