# -*- codeing = utf-8 -*-
# @time :2023/3/9 19:23
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 电话号码的字母组合.py
# @Software :PyCharm
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        strs = [[], [], ['a', 'b', 'c'], ['d', 'e', 'f'],
                ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'],
                ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        res = []
        if len(digits) == 0:
            return res
        elif len(digits) == 1:
            return strs[int(digits[0])]
        elif len(digits) == 2:
            str1 = strs[int(digits[0])]
            str2 = strs[int(digits[1])]
            for i in range(len(str1)):
                for j in range(len(str2)):
                    res.append(str1[i] + str2[j])
            return res
        elif len(digits) == 3:
            str1 = strs[int(digits[0])]
            str2 = strs[int(digits[1])]
            str3 = strs[int(digits[2])]
            for i in range(len(str1)):
                for j in range(len(str2)):
                    for k in range(len(str3)):
                        res.append(str1[i] + str2[j]+str3[k])
            return res
        elif len(digits) == 4:
            str1 = strs[int(digits[0])]
            str2 = strs[int(digits[1])]
            str3 = strs[int(digits[2])]
            str4 = strs[int(digits[3])]
            for i in range(len(str1)):
                for j in range(len(str2)):
                    for k in range(len(str3)):
                        for n in range(len(str4)):
                            res.append(str1[i] + str2[j]+str3[k]+str4[n])
            return res


# 回溯法:数据结构的深度遍历
"""
    (1)判断输入或者状态是否合法
        if inputor state is None:
            return
    （2）判断递归是否应当结束
        if 
            return some value
    （3）遍历所有可能出现的情况
        尝试下一步的可能性
            stack.push 
        递归
            result = fn(m)
    （4）回溯到上一步
        stack.pop
"""