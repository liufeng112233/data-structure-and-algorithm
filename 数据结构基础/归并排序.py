# -*- codeing = utf-8 -*-
# @time :2022/10/23 10:34
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 归并排序.py
# @Software :PyCharm
def merge(li,mid,low,high):
    i=low
    j=mid+1
    ltmp = []
    while i<=mid and j<=high:  #主要左右两边的都有数
        if li[i]<li[j]:
            ltmp.append(li[i])
            i+=1
        else:
            ltmp.append(li[j])
            j+=1
    while i<=mid:
        ltmp.append(li[i])
        i+=1
    while j<=high:
        ltmp.append(li[j])
    li[low:high+1]=ltmp

li=[2,3,4,5,7,1,3,6,8]
merge(li,0,3,7)
print(li)

# 递归的思想
def merge_sort(li,low,high):
    if low<high: # 至少有两个元素
        mid = (low+high)//2
        merge_sort(li,low,mid)
        merge_sort(li,mid+1,high)
        merge(li,low,mid,high)