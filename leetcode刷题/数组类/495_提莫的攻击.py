# -*- codeing = utf-8 -*-
# @time :2023/3/17 20:26
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 495_提莫的攻击.py
# @Software :PyCharm
class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        timeSeries = [1, 4]
        timeSeries = [1, 2]
        duration = 2
        res = []
        for i in range(len(timeSeries)):
            for j in range(duration):
                res.append(timeSeries[i] + j)
        res = len(set(res))
        return res


class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        # timeSeries = [1, 2, 3, 4]
        # duration = 3
        ans = 0
        zhongdu_timing = 0  # 表示中毒时刻
        for i in range(len(timeSeries)):
            if timeSeries[i] >= zhongdu_timing:
                ans += duration
            else:
                ans += timeSeries[i] + duration - zhongdu_timing
            zhongdu_timing = timeSeries[i] + duration
        return ans
