# -*- codeing = utf-8 -*-
# @time :2023/3/10 22:56
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 19_删除链表的倒数第N个节点.py
# @Software :PyCharm
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        def length(head):  # 计算虚拟列表的节点
            length = 0
            while head:
                length += 1
                head = head.next
            return length

        dummy = ListNode(0, head)
        l = length(head)
        cur = dummy
        for i in range(1, l - n + 1):
            cur = cur.next
        cur.next = cur.next.next
        return dummy.next


# 采用快慢指针，保持快指针和慢指针之间的距离为n，当快指针到边界时，慢指针搞好到n处
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0, head)
        slow, fast = dummy, dummy
        for i in range(n + 1):
            fast = fast.next
        while fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next
