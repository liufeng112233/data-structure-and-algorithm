# -*- codeing = utf-8 -*-
# @time :2023/3/31 20:38
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 203_移除列表元素.py
# @Software :PyCharm
# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Solution(object):
#     def removeElements(self, head, val):
#         """
#         :type head: ListNode
#         :type val: int
#         :rtype: ListNode
#         """
#         pre = ListNode(0)
#         pre.next = head
#         p = head
#         while p:
#             if p.val == val:
#                 pre.next = p.next
#                 p = p.next
#             else:
#                 pre = p
#                 p = p.next
#         while head:
#             if head.val == val:
#                 head = head.val
#             else:
#                 return head
#         return head


class Solution(object):
    def removeElements(self, head, val):
        pre = ListNode(0, head)  # 添加虚拟节点
        pre.next = head
        ans = pre
        while pre.next:
            if pre.next.val != val:
                pre = pre.next
            else:
                pre.next = pre.next.next
        return ans.next


# 双指针方法
class ListNode(object):
    def __init__(self,val,next=None):
        self.val = val
        self.next = None
class Solution:
    def removeElements(self, head, val):
        # 够着虚拟节点，后面输出就只虚拟节点。next
        pre= ListNode(0,head)
        cur = head  # 块节点
        last= pre  # 落后一个节点
        while cur:
            if cur.val ==val:
                last.next = cur.next
            else:
                last = last.next
            cur = cur.next
        return pre.next


head = [1, 2, 6, 3, 4, 5, 6]
val = 6
y = Solution()
res = y.removeElements(head, val)
