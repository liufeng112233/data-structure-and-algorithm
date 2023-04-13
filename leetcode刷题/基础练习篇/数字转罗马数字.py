# -*- codeing = utf-8 -*-
# @time :2023/3/8 21:02
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 数字转罗马数字.py
# @Software :PyCharm


# 方法1 采用字典的方式
class Solution:
    def intToRoman(self, num):
        # 构件数值表。实现不同数字的匹配
        # 将整数一次按最大的书写：1994=1000+900+90+4
        hashmap_value = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        hashmap_key = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        res = ''
        for step, key in enumerate(hashmap_key):
            if num // key != 0:
                count = num // key  # 计算有多少个改key下罗马数字
                res += hashmap_value[step] * count
                num %= key
        return res


# 采用暴力匹配算法
# 主要是分别表示个位数、十位数、百位数
class Solution:
    def intToRoman(self, num):
        data1_9 = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        data10_90 = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        data100_900 = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        data1000_3000 = ["", "M", "MM", "MMM"]  # 1000，2000，3000
        cout4 = num//1000
        cout3 = num%1000//100
        cout2 = num%100//10
        cout1 = num%10
        return data1000_3000[cout4]+data100_900[cout3]+data10_90[cout2]+data1_9[cout1]
