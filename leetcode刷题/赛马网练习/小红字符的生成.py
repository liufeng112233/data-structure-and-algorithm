# -*- codeing = utf-8 -*-
# @time :2023/4/7 9:33
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 小红字符的生成.py
# @Software :PyCharm
n = 1
dic = {1: 'a', 2: 'b', 4: 'c', 8: 'd', 16: 'e', 32: 'f', 64: 'g', 128: 'h', 256: 'i', 512: 'j'}
res = ''
len_x = len(dic)
for i in range(len_x - 1, -1, -1):
    if 2**i == n:
        res += dic[2 ** i]
        break
    if 2**i < n:
        res += dic[2 ** i]
        n = n - 2**i
print(res)

# 9a --> 最短 --->
# b --> aa , c --> aaaa, d --> aaaaaaaa
# 最终的数目就是在 1 2 4 8 16 组合
# 比如 5 --> 4 + 1 ca
# init = 'a'
# num = int(input())
# pre = 1
# res = [1]
# out = ''   # 字符串的依次叠加，使用而进制的方式
# while(pre < 1000):
#     pre = pre * 2
#     res.append(pre)
# for i in range(len(res)-1,-1,-1):
#     if res[i] == num:
#         out += chr(ord('a')+i)  # 二进制转化
#         break
#     if res[i] < num:
#         out += chr(ord('a')+i)
#         num = num - res[i]
# print(out)
