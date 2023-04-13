# -*- codeing = utf-8 -*-
# @time :2023/3/13 21:57
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 链表拼接.py
# @Software :PyCharm
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1, l2):
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        prev.next = l1 if l1 is not None else l2

        return prehead.next


l1 = [1, 2, 4]
l2 = [1, 3, 4]
y = Solution()

l1 =ListNode(l1)
l2 =ListNode(l2)
res = y.mergeTwoLists(l1, l2)
