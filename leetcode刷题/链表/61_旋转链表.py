# -*- codeing = utf-8 -*-
# @time :2023/4/11 20:48
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 61_旋转链表.py
# @Software :PyCharm
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head, k):
        # 空链表或者只有一个数，或者k=0时返回就是原始链表
        if k == 0 or not head or not head.next:
            return head
        # 计算链表的长度
        n = 1
        cur = head
        while cur.next:
            cur = cur.next
            n += 1
        # 获取移动数据的长度，进行余数处理
        if k % n == 0:
            return head
        else:
            cur.next = head  # 形成链表环,此时为节点的next指头结点
            num = n-k%n
            while num:
                cur=cur.next
                num-=1
            ret = cur.next
            cur.next = None
            return ret

# 快慢指针
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head, k):
        if k == 0 or not head or not head.next:
            return head
        curl= head
        i= 1
        while curl.next:
            curl = curl.next
            i+=1
        k = int(k%i)  #剔除周期性
        slow =head
        fast = head
        for _ in range(k):
            fast = fast.next
        while fast.next:
            fast=fast.next
            slow = slow.next
        if slow.next:
            temp = slow.next   # 输出此时的temp就是后面k->n的数据再回到head去
            slow.next = None
            fast.next = head   # 将后面的为节点和头结点相连，形成链表环，在采用temp切开输出皆可
        else:
            return head
        return temp    # 此时slow.next就是聊表的开头
