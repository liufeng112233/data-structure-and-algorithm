# -*- codeing = utf-8 -*-
# @time :2023/4/3 21:13
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 输入输出.py
# @Software :PyCharm
import sys
a= list(map(int, input().split()))  #读入一行列表
# 单行输入 4 5
n, m = map(int, sys.stdin.readline().strip().split())
# 赛马的直接读取，多行输入获取相应的数值，同时数据放入一个列表中存储
a, b = [int(i) for i in input().split()]
list = []
for i in range(3):
    list.append([int(i) for i in input().split()])
    print(list)
# 多行输入：把所有行合在一个列表中，采用sys读取
import sys

list = []
list_new = []
for line in sys.stdin:
    list_new = line.split()
    list.append(list_new)
    print(list)
# 输出[[1,2],[2,3]]
import sys

list = []
list_new = []
for line in sys.stdin:
    list_new = line.split()
    list.extend(list_new)  # 注意extend是在一个表后面的不断的增加（1，n），append是形成的list==>(n,m)
    print(list)
# 输出一个列表连输一行输出[1,2,2,3]
#

# 构
# 输出[[1,2],[2,3]]


# 多行输入时，要使用迭代器进行每行遍历，并指定结束方式，这个方式慎用
# 使用map（映射）将以空格分割的字符串强转为整形，并保存在列表当中
"""
    输入：
    1 2 3
    4 5 6
    输出：
    1 4 
    2 5
    3 5
"""
endstr = ""
st = []  # 输出是list[]，读取数据输出[[1,2,3],[4,5,6]]
for line in iter(input, endstr):
    li = list(map(int, line.split()))
    st.append(li)   # 形成列表
"""
    数据读取方式二
    arr = []
while True:  # 针对连续输入多个测试样例
    s = input()
    if s != "":
        arr.append(list(map(int, s.split())))
        # print("a", arr)
    else:
        break
"""
for i in range(len(st[0])):
    for j in range(len(st)):
        if i < len(st) - 1:  # 打印空格，在列边界的前一个需要打印空格
            # print（）中的end可以指定结束方式，默认换行结束，
            # 则下一次print打印在下一行
            print(str(st[j][i]) + " ", end="")
        else:
            print(str(st[j][i]))
    print()

arr = []
while True:  # 针对连续输入多个测试样例
    s = input()
    if s != "":
        arr.append(list(map(str, s.split())))
        # print("a", arr)
    else:
        break