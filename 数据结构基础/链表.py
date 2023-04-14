# -*- codeing = utf-8 -*-
# @time :2023/2/13 9:56
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 链表篇.py
# @Software :PyCharm
class Node:
    def __init__(self,item):
        self.item = item   # 数据域
        self.next = None   # 指向下一个数据额指针

a=Node(1)
b=Node(2)
c=Node(3)
a.next = b
b.next = c
print(a.next.next.next.item)

"""
    创建链表
        (1)头插法
"""
# 头插法
def create_linklist_head(li):
    head = Node(li[0])
    for element in li[1:]:
        node = Node(element)
        node.next = head
        head = node
    return head
# 尾插法
def create_linklist_tail(li):
    head = Node(li[0])
    tail = head
    for element in li[1:]:
        node = Node(element)
        tail.next = node
        tail = node
    return head
def print_linklist(lk):
    while lk:
        print(lk.item,end=',')
        lk = lk.next

lk =create_linklist_head([1,2,3])
print_linklist(lk)
li = create_linklist_tail([1,2,3,4,5])
print_linklist(li)