# -*- codeing = utf-8 -*-
# @time :2023/3/31 21:48
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 237_删除链表中的节点.py
# @Software :PyCharm
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # 将后面一个节点删除，但是实际需要删除前一个结点。
        # 所以将后一个节点的覆盖到前一个结点，这样假装删除node结点。
        # 然后让后一个节点删除代替node删除
        node.val = node.next.val
        node.next = node.next.next