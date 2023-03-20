# -*- codeing = utf-8 -*-
# @time :2023/2/28 10:44
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 最大公约数.py
# @Software :PyCharm
"""
    欧几里得算法：gcb(a,b) = gcb(b,a mode b)
    eg:gcb(60,21) = gcb(21,18)=gcb(18,3) =gcb(3,0)

"""


# 递归方式
def gcb(a, b):
    if b == 0:
        return a
    else:
        return gcb(b, a % b)


def gcb2(a, b):
    while b > 0:
        r = a % b
        c = b
        b = r
    return a


# 实现分数计算
class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        x = self.gcd(a,b)
        self.a /= x
        self.b /= x

    def gcd(self, a, b):
        while b > 0:
            r = a % b
            a = b
            b = r
        return a

    def zgs(self, a, b):
        # 12 16 -> 4
        # 3*4*4=48
        x = self.gcd(a, b)
        return a * b / x

    def __add__(self, other):
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        fenmu = self.zgs(b, d)
        fenzi = a * fenmu / b + c * fenmu / d
        return Fraction(fenzi, fenmu)



    def __str__(self):
        return "%d/%d" % (self.a, self.b)


a = Fraction(1,3)
b = Fraction(1,2)
print(a+b)