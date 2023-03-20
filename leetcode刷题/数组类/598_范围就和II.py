# -*- codeing = utf-8 -*-
# @time :2023/3/20 19:31
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 598_范围就和II.py
# @Software :PyCharm
class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        m = 3
        n = 3
        ops = [[2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3], [2, 2], [3, 3], [3, 3], [3, 3]]
        ans = [[[0] for _ in range(n)] for _ in range(m)]
        mina, minb = m, n
        for a, b in ops:
            mina = min(mina, a)
            minb = min(minb, b)
        return mina * minb
