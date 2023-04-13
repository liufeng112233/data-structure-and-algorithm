# -*- codeing = utf-8 -*-
# @time :2023/4/5 20:16
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 小红踏前斩.py
# @Software :PyCharm
#python代码
#踏前斩最小数量：分两种情况讨论，两个相邻的怪物或者最小血量的两个怪物
#核心思想：1.如果第二个怪物的血量大于第一个怪物血量的两倍，如2,5，这时最小次数主要看
#第二个怪物的血量，最小次数为(5+1)//2
#2.如果第二个怪物的血量小于等于第一个怪物血量的两倍，如2,3，这时首先对第一个怪物释放
#技能（因为这样可以同时打到两个怪物），第二个怪物死后，为消灭第一个怪物，对第一个怪
#物的前一个怪物释放技能打死第一个怪物。
#注意i==0时要分类讨论
#求最小的两个值时，首先给min1赋值为a[0]，因为后面循环i从0变到n-2，那么（i+1）刚好就
#是除了第一个元素之外的n-1个元素
n = int(input())
a = list(map(int,input().split()))
min1 = a[0]
min2 = float('inf')
ans = float('inf')
for i in range(n-1):
    if i == 0:
        if a[1] <= 2*a[0]:
            count = a[0]
        else:
            count = (a[1]+1)//2
    else:
        if a[i+1] > 2*a[i]:
            count = (a[i+1]+1)//2
        else:
            # a[i]死亡包括对a[i+1]的攻击还有自身的剩余血量
            count = (a[i+1]+1)//2+(a[i]-(a[i+1]+1)//2+1)//2
    ans = min(ans,count)
    m = (a[i+1]+1)//2    #求杀死a[i+1]怪兽的最小踏前斩次数
    if m < min1:
        min2 = min1
        min1 = m
    elif m < min2:
        min2 = m
print(min(ans,min1+min2))