# -*- codeing = utf-8 -*-
# @time :2023/4/6 21:54
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 塔子哥的选择题.py
# @Software :PyCharm
import sys

n = int(input())
select = list(map(str, input().split()))
answer = list(map(str, input().split()))
score = 0
for i in range(n):
    len_select = len(select[i])
    len_answer = len(answer[i])
    # 判断是都长度相同，相同在进行内部的数据比对，不相等在判断是否小于，大与直接等于0
    if len_select == len_answer:
        falg = 0
        for j in range(len(select[i])):
            if select[i][j] in answer[i]:
                falg+=1
        if falg==len(select[i]):
            score+=3
    elif len_select < len_answer:
        falg=0
        for j in range(len(select[i])):
            if select[i][j] in answer[i]:
                falg+=1
        if falg==len(select[i]):
            score += 1
print(score)
