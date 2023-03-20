# -*- codeing = utf-8 -*-
# @time :2023/3/17 9:28
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : P1001_k优雅阈值.py
# @Software :PyCharm

# n , k = list(map(int , input().split()))
# nums = list(map(int , input().split()))
a = [1, 2, 3, 1, 1, 2, 1, 3, 1]
k = 3
n = len(a)
# 桶
d = [0 for i in range(10005)] # 存储出现的次数
# ans记录答案
ans = 0
# i 是左端点,j是右端点
i = 0
for j in range(n):
    # 新增一个点,记录出现次数
    d[a[j]] += 1
    # 如果有数出现次数大于等于k,那么一定是a[j]
    while d[a[j]] >= k:
        #统计答案,根据<单调性>
        #以i为起点的合法区间一定是:[i , j],[i , j + 1],...,[i,n]
        ans += n - j
        #移动左端点
        d[a[i]] -= 1
        i += 1
print(ans)