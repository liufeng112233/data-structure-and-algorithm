# -*- codeing = utf-8 -*-
# @time :2023/3/24 21:49
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 22_括号的生成.py
# @Software :PyCharm
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        # 回溯加枝剪
        res = []
        cur_str = ''

        def dfs(cur_str, left, right):
            '''
            :param cur_str:   根节点到叶子节点的路径字符串
            :param left:   左括号还可以使用的个数
            :param right:  右括号还可也使用的个数
            :return:
            '''
            if left < 0 or left > right:  # 出现类似 ()) )) 这种格式都是错误的不用再继续了
                return
            if left == 0 and right == 0:
                res.append(cur_str)
                return
            if left > 0:
                dfs(cur_str + '(', left - 1, right)
            if right > 0:
                dfs(cur_str + ')', left, right - 1)

        dfs(cur_str, n, n)
        return res


y = Solution()
n=3
res = y.generateParenthesis(n)