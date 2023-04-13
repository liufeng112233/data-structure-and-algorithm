# -*- codeing = utf-8 -*-
# @time :2023/3/27 9:39
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 23_合并K个升序链表.py
# @Software :PyCharm

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # 构建虚拟头结点
        lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
        head = ListNode(0)
        end = head
        arr = []
        for node in lists:
            print(node)
            while node:
                arr.append(node.val)
                node = node.next
        arr.sort()
        for num in arr:
            curnode = ListNode(num)
            end.next=curnode
            end = curnode
        return head.next