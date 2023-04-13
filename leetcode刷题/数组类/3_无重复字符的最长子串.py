# -*- codeing = utf-8 -*-
# @time :2023/4/10 10:54
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 3_无重复字符的最长子串.py
# @Software :PyCharm
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        # 首先检录一个数据集set
        SET_data = set()
        n = len(s)
        # 指针用于指示数据集，边界问题
        rk, ans = -1, 0
        for i in range(n):
            if i != 0:
                SET_data.remove(s[i - 1])
            while rk + 1 < n and s[rk + 1] not in SET_data:
                # 移动指针
                SET_data.add(s[rk + 1])
                rk += 1
            ans = max(ans, rk - i + 1)
        return ans

y = Solution()
s = "abcabcbb"
res = y.lengthOfLongestSubstring(s)


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        lst = []
        n = len(s)
        ans = 0
        for i in range(n):
            while s[i] in lst:
                del lst[0]  # 队首元素出队
            lst.append(s[i]) # 排除重复元素后 新元素入队
            ans = max(ans, len(lst))
        return ans