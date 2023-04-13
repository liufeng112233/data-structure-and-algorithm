# # # -*- codeing = utf-8 -*-
# # # @time :2023/4/10 9:24
# # # @Project: data-structure-and-algorithm
# # # @Author : 刘风
# # # @File : 罪犯转移.py
# # # @Software :PyCharm
# import sys  # 前缀和
#
# while True:
#     try:
#         n, t, c = [int(i) for i in input().split()]
#         # n: 罪犯数量，t:罪犯的最大值，c:几名连续的罪犯
#         a = list(map(int, input().split()))
#         # print(a)
#         count = 0
#         arr = [0] * n
#         arr[0] = a[0]
#         for i in range(1, n):
#             arr[i] = arr[i - 1] + a[i]
#         # 采用窗口
#         left, right = 0, c-1
#         while right<n:
#             if arr[right] - arr[left] <= t:
#                 count += 1
#             left += 1
#             right += 1
#         print(count)
#     except:
#         break
#
# """
#     维持滑移窗口的长度不变
# """
# import sys
#
# while True:
#     try:
#         n, t, c = [int(i) for i in input().split()]
#         a = list(map(int, input().split()))
#         # 构建滑移窗口
#         l, r = 0, c - 1
#         res = 0
#         sum_num = 0
#         while r < n:
#             if l == 0:
#                 sum_num = sum(a[l:r + 1])
#             else:
#                 sum_num = sum_num + a[r] - a[l - 1]
#             if sum_num <= t:
#                 res += 1
#             l += 1
#             r += 1
#         print(res)
#     except:
#         break

