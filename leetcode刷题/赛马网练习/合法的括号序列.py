# -*- codeing = utf-8 -*-
# @time :2023/4/6 20:33
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 合法的括号序列.py
# @Software :PyCharm
# (????(()??)(??)?))))
"""
    链接：https://www.nowcoder.com/questionTerminal/cd3c583ac7054a18b164fbd4ec3247c4
假设字符串长度为 n，可以考虑使用动态规划求解。令 dp[i][j] 表示前 i 个字符中，左括号比右括号多 j 个的方案数。考虑第 i+1 个字符：
    如果是左括号，则 dp[i+1][j+1] = dp[i][j]。
    如果是右括号，则 dp[i+1][j-1] = dp[i][j]。
    如果是问号，则既可以代表左括号，也可以代表右括号，因此 dp[i+1][j+1] = dp[i][j] + dp[i+1][j-1]。
最终答案即为 dp[n-1][0]，表示左右括号数量相等的方案数。  可以设置0边界
需要注意的是，由于原始字符串中可能存在 ? 字符，因此需要初始化 dp[0][1] = 1，并将剩余的 dp[0][j] 和 dp[i][j] 的值都设为 0。
"""
s = input()
n = len(s)
if s[0] == ')':
    print(0)
else:
    dp = [[0 for _ in range(n)] for _ in range(n)]
    dp[0][1] = 1  # 初始为？或者（，在的第二个起码是存在合法括号的
    for i in range(1, n):  # 从第二个符开始计算
        if s[i] == '(' or s[i] == '?':
            for j in range(1, n):
                if j > i + 1 or j > n - i - 1:   #这种不匹配了，
                    break
                dp[i][j] += dp[i - 1][j - 1]
                dp[i][j] %= (1e9 + 7)   # 数据大太大进行取模
        if s[i] == ')' or s[i] == '?':
            for j in range(0, n - 1):   # 启始边界可能是（，所以【0，n】
                if j > i + 1 or j > n - i - 1:  # 大于是（括号太多，后面的数据无法正常匹配了
                    break
                dp[i][j] += dp[i - 1][j + 1]
                dp[i][j] %= (1e9 + 7)

    print(int(dp[n - 1][0]))