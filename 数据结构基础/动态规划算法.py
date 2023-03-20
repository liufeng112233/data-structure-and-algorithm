# -*- codeing = utf-8 -*-
# @time :2023/2/22 11:13
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 动态规划算法.py
# @Software :PyCharm
"""
    动态规划：
        1、斐波那契数列，采用地推公式
        2、什么问题可以动态规划
            （1）最优子结构：原问题中最优解涉及多少个子问题；在确定最优解使用哪些子问题时，需要考虑多少种选择
            （2）重叠子问题


"""

# 菲波那切数列
# 递归方式
import time


def fibnacci(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fibnacci(n - 1) + fibnacci(n - 2)


# 非递归方式
def fibnacci_no_recusion(n):
    f = [0, 1, 1]
    for i in range(n - 2):
        num = f[-1] + f[-2]
        f.append(num)
    return f[n]


print(fibnacci(20))

"""
     钢条切割问题
"""


# 时间监视器
def cal_time(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        result = func(*args, **kwargs)
        t2 = time.time()
        print("%s running time: %s secs." % (func.__name__, t2 - t1))
        return result

    return wrapper


# p = [1, 1, 5, 8, 9, 10, 17, 17, 20, 21, 23, 24, 26, 27, 27, 28, 30, 33, 36, 39, 40]


p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]


# @cal_time
def cut_rod_recursion1(p, n):
    if n == 0:
        return 0
    else:
        res = p[n]
        for i in range(1, n - 1):
            res = max(res, cut_rod_recursion1(p, i) + cut_rod_recursion1(p, n - i))
        return res


# @cal_time
def cut_rod_recursion(p, n):
    if n == 0:
        return 0
    else:
        res = 0
        for i in range(1, n + 1):
            res = max(res, p[i] + cut_rod_recursion(p, n - i))
        return res


print(cut_rod_recursion1(p, 10))
print(cut_rod_recursion(p, 10))


# 动态规划——自底向上循环方法，res = max(p_i,r_(n-i))边界条件[1,n]
def cut_rod_dp(p, n):
    r = [0]  # 边界条件
    for i in range(1, n + 1):  # 循环n次  ,这里的i表示n的变值
        res = 0
        for j in range(1, i + 1):
            res = max(res, p[j] + r[i - j])
        r.append(res)
    return r[n]


# 动态问题切割解——重构解。不仅输出最优解，还输出最优切割方案
def cut_rod_extend(p, n):
    r = [0]
    s = [0]
    for i in range(1, n + 1):  # 循环n次  ,这里的i表示n的变值
        res_r = 0  # 记录借个的最优解
        res_s = 0  # 价格最大值对应的方案的左边不切割部分的长度
        for j in range(1, i + 1):
            if p[j] + r[i - j] > res_r:
                res_r = p[j] + r[i - j]
                res_s = j
        r.append(res_r)
        s.append(res_s)
    return r[n], s
def cut_rod_solution(p,n):    # 分的方案
    r,s = cut_rod_extend(p,n)
    ans=[]
    while n>0:
        ans.append(s[n])
        n = n-s[n]
    return ans
print(cut_rod_solution(p,7))

p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]
r, s = cut_rod_extend(p, 10)
print(s)
