# -*- codeing = utf-8 -*-
# @time :2023/4/13 22:18
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 206_反转链表.py
# @Software :PyCharm

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head):
        # 直接使用栈进行
        stack = []
        cur= head
        while cur:
            stack.append(cur)
            cur = cur.next
        reverse = ListNode(-1)  # 制作输出节点
        dummy = reverse  # 方便返回
        while stack:
            node = stack.pop()
            dummy.next = node    # 数据进链表
            dummy = dummy.next   # 指针更新
        dummy.next = None  # 防止成环
        return reverse.next
