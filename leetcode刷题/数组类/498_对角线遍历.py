# -*- codeing = utf-8 -*-
# @time :2023/3/22 20:53
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 498_对角线遍历.py
# @Software :PyCharm
class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        # mat = [[1,2],[3,4]]
        mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        m, n = len(mat), len(mat[0])
        res = []
        # 直接蛇皮走位遍历
        for i in range(m + n):
            if i % 2 == 0:  # 自下到上的遍历方式,偶数时
                if i < m:
                    j, k = i, 0
                else:
                    j, k = m - 1, i - m + 1
                while j >= 0 and k < n:
                    res.append(mat[j][k])
                    j -= 1
                    k += 1
            else:  # 奇数时是自上而下
                if i < n:
                    j, k = 0, i
                else:
                    j, k = i - n + 1, n - 1
                while j < m and k >= 0:
                    res.append(mat[j][k])
                    j += 1
                    k -= 1
        return res


'''
    首先确定对角线的两种方向；
    2、假设每次按照原方向行进，遇到出界的时候，假如是遇到了上下边界，那么优先往右拐，
    如果不行再往下拐，假如是遇到了左右边界，那么优先往下拐，如果不行再往右拐；
    3、没出界就继续走
'''


class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        mat = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
        ans = []
        move = [[-1, 1], [1, -1]]  # move[0]上：行减一列加一:     move[1]下：行加一列减一
        j, r, c = 0, 0, 0
        maxL = len(mat) * len(mat[0])  # 一共需要走多少步
        for i in range(maxL):
            ans.append(mat[r][c])
            x, y = r + move[j][0], c + move[j][1]  # 先按方向走，不行改变方向，记录此时的起点位置
            if x < 0 or x == len(mat):  # 向上移动
                # 此时超过上下边界，优先向右进一，不行在向下进一，同时move的方向要变动
                if c < len(mat[0]) - 1:  # 向右进一（上边界）
                    c += 1
                else:  # 向下进一（左边界）
                    r += 1
                j = 1 - j  # 这里限定了j的取值范围,改变移动方向
            elif y < 0 or y == len(mat[0]):  # 向下移动
                # 超过左右边界，优先向下走，如果不行在右走，同时move方向变动
                if r < len(mat) - 1:
                    r += 1
                else:
                    c += 1
                j = 1 - j
            else:
                r = x
                c = y
            return ans
