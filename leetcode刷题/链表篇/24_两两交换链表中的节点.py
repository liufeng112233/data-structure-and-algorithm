# -*- codeing = utf-8 -*-
# @time :2023/4/13 21:27
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 24_两两交换链表中的节点.py
# @Software :PyCharm

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
    思路：
        
"""


class Solution:
    def swapPairs(self, head):
        if not head and not head.next:
            return head
        p = ListNode(-1)  # 构建虚拟节点
        # 用stack保存每次迭代的两个节点
        # head指向新的p节点，函数结束时返回head.next即可
        cur, head, stack = head, p, []
        while cur and cur.next:
            # 将两个节点放入栈中
            stack.append(cur)
            stack.append(cur.next)
            cur = cur.next.next  # 当前节点向下走两个节点
            p.next = stack.pop()
            p.next.next = stack.pop()
            p = p.next.next  # 更新的节点位置
        # 注意边界条件，当链表长度是奇数时，cur就不为空
        if cur:
            p.next = cur
        else:
            p.next = None
        return head.next


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


"""
    思路：

"""


# 迭代实现
class Solution1:
    def swapPairs(self, head):
        if not head:
            return head
        elif not head.next:
            return head
        p = ListNode(-1)
        a, b, p.next, temp = p, p, head, p  # 创建a，b两个指针，这里还需要一个tmp指针
        while b.next and b.next.next:
            # a 前进一位，b前进两位
            a, b = a.next, b.next.next
            # 这步很关键，tmp指针用来处理边界条件的
            # 假设链表是1->2->3->4，a指向1，b指向2
            # 改变a和b的指向，于是就变成2->1，但是1指向谁呢？
            # 1是不能指向2的next，1应该指向4，而循环迭代的时候一次处理2个节点
            # 1和2的关系弄清楚了，3和4的关系也能弄清楚，但需要一个指针来处理
            # 2->1，4->3的关系，tmp指针就是干这个用的
            temp.next, a.next, b.next = b, b.next, a
            # 现在链表就变成2->1->3->4
            # tmp和b都指向1节点，等下次迭代的时候
            # a就变成3，b就变成4，然后tmp就指向b，也就是1指向4
            temp, b = a, a
        return p.next


class Solution2(object):
    def swapPairs(self, head):
        # 递归的终止条件
        if not (head and head.next):
            return head
        # 假设链表是 1->2->3->4
        # 这句就先保存节点2
        tmp = head.next
        # 继续递归，处理节点3->4
        # 当递归结束返回后，就变成了4->3
        # 于是head节点就指向了4，变成1->4->3
        head.next = self.swapPairs(tmp.next)
        # 将2节点指向1
        tmp.next = head
        return tmp
