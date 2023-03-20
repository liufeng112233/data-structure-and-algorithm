# -*- codeing = utf-8 -*-
# @time :2023/2/13 11:27
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 哈希表.py
# @Software :PyCharm

class LinkList:   # 链表存储
    class Node:
        def __init__(self, item=None):  # 链表
            self.item = item

            self.next = None

    class LinkListIterator:
        def __init__(self, node):
            self.node = node

        def __next__(self):
            if self.node:
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.item
            else:
                raise StopIteration    # 迭代停止

        def __iter__(self):
            return self

    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)  # 列表写法

    def append(self, obj):   # obj对象
        s = LinkList.Node(obj)
        if not self.head:   # 链表空
            self.head = s
            self.tail = s
        else:
            self.tail.next = s
            self.tail = s

    def extend(self, iterable):
        for obj in iterable:
            self.append(obj)

    def find(self, obj):
        for n in self:   # shlf自己对象
            if n == obj:
                return True
        else:
            return False

    def __iter__(self):   # 迭代器，方便for循环
        return self.LinkListIterator(self.head)

    def __repr__(self):  # 字符串转化
        return "<<"+", ".join(map(str, self))+">>"

# 类似于集合的结构
class HashTable:
    def __init__(self, size=101):   # size 哈希表的长度
        self.size = size
        self.T = [LinkList() for i in range(self.size)]  # 就是一个列表

    def h(self, k):
        return k % self.size   # 哈希函数,计算余数<<余数，value>>

    def insert(self, k):
        i = self.h(k)    # 计算哈希值。计算k查到i的位置上
        if self.find(k):  #判断集合中是否有该元素
            print("Duplicated Insert.") # 找到输出重复插入
        else:
            self.T[i].append(k)     # 没有找到，插入元素到列表中

    def find(self, k):  # 查找函数
        i = self.h(k)
        return self.T[i].find(k)   # T[i]是链表中额数值find（k）


ht = HashTable()

ht.insert(0)
ht.insert(1)
ht.insert(3)
ht.insert(102)
ht.insert(508)
ht.insert(203)
print(",".join(map(str, ht.T)))
print(ht.find(203))


"""
    哈希表的应用实例，集合、字典
"""
# 字符串可以转化为整数
# md5算法，密码算法

