# -*- codeing = utf-8 -*-
# @time :2023/3/18 17:25
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 661_图片平滑器.py
# @Software :PyCharm
class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        # img = [[100, 200, 100], [200, 50, 200], [100, 200, 100]]
        m, n = len(img), len(img[0])  # 两层尺寸
        ans = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                tot, num = 0, 0
                # 下面开始计算相对应的内的均值
                for x in range(max(i - 1, 0), min(i + 2, m)):  # 边界问题
                    for y in range(max(j - 1, 0), min(j + 2, n)):
                        tot += img[x][y]
                        num += 1
                ans[i][j] = tot // num
        return ans
