# -*- codeing = utf-8 -*-
# @time :2023/3/8 21:34
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 最小公共前缀.py
# @Software :PyCharm

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = ""
        for tmp in zip(*strs):  # zip(*strs)把字符串列表转换成一个元组的列表，及是进行list的纵向对堆叠，tmp表示的同一列的所有元素
            print(tmp)
            tmp_set = set(tmp)  # 利用集合元素的唯一性，进行相同元素的去除
            print(tmp_set)
            if len(tmp_set) == 1:  # 如果只有自由一个值
                res += tmp[0]
            else:
                break
        return res


# 方法二
def longest_common_prefix(strs):
    if not strs:  # 如果为空直接返回“”
        return ""
    prefix = strs[0]  # 采用第一个字符进行匹配的其实字符
    for s in strs[1:]:
        # 当匹配上是停止
        while not s.startswith(prefix):  # 用于判断字符串是否以指定前缀开头，如果是则返回 True，否则返回 False
            prefix = prefix[:-1]  # 一次减少一个末尾字符
            if not prefix:
                return ""
    return prefix


strs = ['flower', 'flow', 'flight']

res = longest_common_prefix(strs)
