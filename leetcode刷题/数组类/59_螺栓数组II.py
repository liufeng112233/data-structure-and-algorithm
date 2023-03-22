# -*- codeing = utf-8 -*-
# @time :2023/3/22 20:05
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 59_螺栓数组II.py
# @Software :PyCharm
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        # 采用二维数据的查询方式进行构建
        res = [[0 for _ in range(n)] for _ in range(n)]   # 构建存储矩阵
        if n == 1:
            return [[1]]
        if n == 0:
            return [[]]
        up, down = 0, n - 1
        left, right = 0, n - 1
        while True:  # 利用前一步的数计算后一步的数值
            for i in range(left, right + 1):
                res[up][i] = res[up][i - 1] + 1  # 左边数加一，i=0时，后变数为0，此时刚好满足
            up += 1
            if up > down:
                break
            for i in range(up, down + 1):  # 上面计算下面
                res[i][right] = res[i - 1][right] + 1
            right -= 1
            if right < left:
                break
            for i in range(right, left - 1, -1):
                res[down][i] = res[down][i + 1] + 1  # 右边计算左边
            down -= 1
            if down < up:
                break
            for i in range(down, up - 1, -1):
                res[i][left] = res[i + 1][left] + 1   # 下边计算上边
            left += 1
            if left > right:
                break
