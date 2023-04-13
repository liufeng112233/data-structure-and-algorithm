# -*- codeing = utf-8 -*-
# @time :2023/3/31 22:02
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 83_删除排序链表的重复元素.py
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
        if not head:
            return head
        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next=cur.next.next
            else:
                cur =cur.next
        return head

# 由于提供的原始链表中不存在初始初始化链表
# 尝试构建初始化结点

class Node(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        pre = Node(None,head)  # 构建一个虚拟的空节点
        last = pre  # 保存初始结点，输出last.next
        # 这样避免了头结点的查询遍历
        while pre.next:
            if pre.val == pre.next.val:
                pre.next = pre.next.next
            else:
                pre = pre.next
        return last.next





