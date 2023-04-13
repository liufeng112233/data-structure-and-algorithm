# # class Solution:
# #      def isMatch(self, s, p):
s = "abbba"
p = "ab*a"


# cache = [[False] * (len(s) + 1) for _ in range(len(p) + 1)]  # 状态存储二维数组
# cache[0][0] = True
# for i in range(1, len(p)):
#     cache[i + 1][0] = cache[i - 1][0] and p[i] == "*"
# for i in range(len(p)):
#     for j in range(len(s)):
#         if p[i] == "*":
#             cache[i + 1][j + 1] = cache[i][j + 1] or cache[i - 1][j + 1]
#             if p[i - 1] == s[j] or p[i - 1] == ".":
#                 cache[i + 1][j + 1] |= cache[i + 1][j]
#         else:
#             cache[i+1][j+1]=cache[i][j] and (p[i]==s[j] or p[i]==".")

# 解题思路1，官方解答，动态规划问题
def isMatch(s, p):
    # 主要还是对于分析'.'和字符'*'的边界问题
    m, n = len(s), len(p)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True

    def match(i, j):  # 第i、j字符数是否相同，
        if i == 0:  # 这里s[0]空字符，没有匹配为问题
            return False
        if p[j - 1] == '.':
            return True
        else:
            return s[i - 1] == p[j - 1]

    # *
    for i in range(m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == "*":
                dp[i][j] |= dp[i][j - 2]  # dp[i][j] = dp[i][j - 2] or dp[i][j-1]
                if match(i, j - 1):
                    dp[i][j] |= dp[i - 1][j]
            if match(i, j):
                dp[i][j] |= dp[i - 1][j - 1]

    return dp[m][n]

# 解题思路2

class Solution(object):
    def isMatch(self, s, p):
        if not s and not p:  # s,p 空
            return True
        if not p and s:  # p空
            return False
        if not s and p:  # s 空
            # ' ' match '.*' or 'x*'
            if len(p) > 1 and p[1] == '*' and self.isMatch(s, p[2:]):
                return True
            else:
                return False
        # p!=空 and s!=空
        # p = 'a-z','.', '*'
        if p[0] == '.':
            if len(p) > 1 and p[1] == '*':
                # '.*' match ' '->isMatch(s,p[2:])
                # '.*' match s[1:]->isMatch(s[1:],p[2:])
                # .....
                # '.*. match s -> isMatch(s[len(s):],p[2:])
                for i in range(len(s) + 1):
                    if self.isMatch(s[i:], p[2:]):
                        return True
            # p = '.a-z'，第一个字符任意匹配
            elif self.isMatch(s[1:], p[1:]):
                return True
        else:  # 这里表示p还有*的数据情况
            # p[0]='a-z'
            # p='x*'    其中x表示a-z的字幕
            if len(p) > 1 and p[1] == '*':
                # 'x*' match ' '  -> isMatch(s[1:],p[2:])
                # if s[0]==p[0],'x*' match s[1:] ->isMatch(s[1:],p[2:])
                # 'x*' match s =='xxxxy'
                if self.isMatch(s, p[2:]):  # 这里表示s=空的情况
                    return True
                for i in range(len(s)):
                    if s[i] == p[0]:  # 表示s[i-1]和p都匹配上了，只考虑后面的s[1:]和p[2:]的匹配关系
                        if self.isMatch(s[i + 1:], p[2:]):
                            return True
                    else:
                        break
            else:
                if p[0] == s[0] and self.isMatch(s[1:], p[1:]):
                    return True
        return False
