# -*- codeing = utf-8 -*-
# @time :2023/3/27 20:31
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 707_设计链表.py
# @Software :PyCharm
class ListNode:  # 定义节点
    def __init__(self, val):
        self.data = val  # 定义节点的数值
        self.next = None


class MyLinkedList:

    def __init__(self):  # 初始化
        self.size = 0
        self.head = ListNode(0)

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.size:  # 判断是否超出边界值
            return -1
        cur = self.head  # 从头结点开始循环
        for _ in range(index + 1):  # 由于添加了一个头结点，是的原来的index节点需要下一个节点是才是寻找节点
            cur = cur.next
        return cur.data

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(0, val)  # 就是在头部掺入节点
        # self.size +=1
        # pred = self.head   # 此时第一个是虚拟节点
        # data = ListNode(val)
        # data.next = pred.next
        # pred.next = data  # 依旧保持头结点不改变

    def addAtTail(self, val):  # 末尾添加
        """
        :type val: int
        :rtype: None
        """
        self.addAtIndex(self.size, val)
        pred = self.head
        index = self.size
        self.size += 1
        for _ in range(index):
            pred = pred.next
        data = ListNode(val)
        data.next = pred.next   # 依旧还是采用插入的操作
        pred.next = data

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.size:
            return
        index = max(0, index)
        self.size += 1
        pred = self.head
        for _ in range(index):
            pred = pred.next  # 移动指针，列表的指针只能从开头开始查询，不能直接中间查询
        to_add = ListNode(val)
        to_add.next = pred.next
        pred.next = to_add

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return
        self.size -= 1
        pred = self.head
        for _ in range(index):
            pred = pred.next
        pred.next = pred.next.next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
