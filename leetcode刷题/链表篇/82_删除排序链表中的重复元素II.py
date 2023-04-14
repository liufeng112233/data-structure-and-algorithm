# -*- codeing = utf-8 -*-
# @time :2023/4/2 16:23
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 82_删除排序链表中的重复元素II.py
# @Software :PyCharm
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None and head.next == None:
            return head
        dummy = ListNode(-1000)
        dummy.next = head
        fast = dummy.next
        slow = dummy
        # 构建快慢节点指针
        while fast:
            if fast.next and fast.next.val == fast.val:
                tmp = fast.val
                while fast and tmp == fast.val:
                    fast = fast.next
            else:
                slow.next = fast
                slow = fast
                fast = fast.next
        slow.next = fast
        return dummy.next


class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return head
        dummy = ListNode(None,head)   # 构建虚拟节点
        cur = dummy   # 保存初始虚拟节点
        while cur.next and cur.next.next:  # 当当前节点和下一个节点存在
            if cur.next.val ==cur.next.next.val:   # 当相邻节点相等
                tmp = cur.next.val   #暂存节点值
                while cur.next and cur.next.val ==tmp:     # 利用while的自循环和边界值
                    cur.next = cur.next.nex    # 寻找边界值
            else:
                cur = cur.next
        return dummy.next

