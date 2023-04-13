# -*- codeing = utf-8 -*-
# @time :2023/4/2 17:16
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 430_扁平化多级双向链表.py
# @Software :PyCharm

# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        # 计算链表的最后一个值
        def dfs(node):
            cur = node
            # 记录链表的最后一个节点
            last = None
            while cur:
                nxt = cur.next  # 暂存节点
                if cur.child:
                    child_last = dfs(cur.child)
                    nxt = cur.next
                    # 将node与child相连,双向链表
                    cur.next = cur.child
                    cur.child.prev = cur
                    # 如果nxt不为空，就将last与nxt相连
                    if nxt:
                        child_last.next = nxt
                        nxt.prev = child_last
                    # 将child置空
                    cur.child = None
                    last = child_last
                else:
                    last = cur
                cur = nxt
            return last

        dfs(head)
        return head
