# # # -*- codeing = utf-8 -*-
# # # @time :2023/2/15 9:33
# # # @Project: data-structure-and-algorithm
# # # @Author : 刘风
# # # @File : 二叉树的遍历.py
# # # @Software :PyCharm
class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None


a = BiTreeNode("A")
b = BiTreeNode("B")
c = BiTreeNode("C")
d = BiTreeNode("D")
e = BiTreeNode("E")
f = BiTreeNode("F")
g = BiTreeNode("G")
# 构建有限的二叉树
e.lchild = a
e.rchild = g
a.rchild = c
c.lchild = b
c.rchild = d
g.rchild = f
root = e
print(root.lchild.rchild.data)
"""
    二叉树的遍历
        遍历按照一定的规律变化
"""


# 前序遍历：
def pre_order(root):
    if root:
        print(root.data, end=',')
        pre_order(root.lchild)
        pre_order(root.rchild)


# 中序遍历
def in_order(root):
    if root:
        in_order(root.lchild)
        print(root.data, end=',')
        in_order(root.rchild)


# 后序遍历
def post_order(root):
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data, end=',')


# 层次遍历：层层写，需要队列，多叉树依旧使用\
from collections import deque  # 构建队列函数


def level_order(root):
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        node = queue.popleft()
        print(node.data, end=',')
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)


print("\n前序遍历")
pre_order(root)
print("\n中序遍历")
in_order(root)
print("\n后序遍历")
post_order(root)
print("\n层次遍历")
level_order(root)

#
# """
#     二乘搜索树，查询、删除、插入
# """
# import random
#
#
# class BiTreeNode:
#     def __init__(self, data):
#         self.bf = None
#         self.data = data
#         self.lchild = None
#         self.rchild = None
#         self.parent = None  # 双链表需要
#
#
# class BST:
#     def __init__(self, li=None):
#         self.root = None
#         if li:
#             for val in li:
#                 self.insert_not_rec(val)
#
#     # 插入
#     def insert(self, node, val):
#         if not node:
#             node = BiTreeNode(val)
#         elif val < node.data:
#             node.lchild = self.insert(node.lchild, val)
#             node.lchild.parent = node
#         elif val > node.data:
#             node.rchild = self.insert(node.rchild, val)
#             node.rchild.parent = node
#         return node
#
#     def insert_not_rec(self, val):  # 非迭代方法
#         p = self.root
#         if not p:
#             self.root = BiTreeNode(val)  # 空树处理
#             return
#         while True:
#             if val < p.data:
#                 if p.lchild:  # 如果左孩子存在
#                     p = p.lchild
#                 else:  # 左孩子不存在
#                     p.lchild = BiTreeNode(val)
#                     p.lchild.parent = p
#                     return
#             elif val > p.data:
#                 if p.rchild:
#                     p = p.rchild
#                 else:
#                     p.rchild = BiTreeNode(val)
#                     p.rchild.parent = p
#                     return
#             else:
#                 return
#
#     def query(self, node, val):  # 递归函数查询
#         if not node:
#             return
#         if node.data < val:
#             return self.query(node.rchild, val)
#         elif node.data > val:
#             return self.query(node.lchild, val)
#         else:
#             return node
#
#     def query_no_rec(self, val):
#         p = self.root
#         while p:
#             if p.data < val:
#                 p = p.rchild
#             elif p.data > val:
#                 p = p.lchild
#             else:
#                 return p
#         return None
#
#     # 前序遍历：
#     def pre_order(self, root):
#         if root:
#             print(root.data, end=',')
#             self.pre_order(root.lchild)
#             self.pre_order(root.rchild)
#
#     # 中序遍历
#     def in_order(self, root):
#         if root:
#             self.in_order(root.lchild)
#             print(root.data, end=',')
#             self.in_order(root.rchild)
#
#     # 后序遍历
#     def post_order(self, root):
#         if root:
#             self.post_order(root.lchild)
#             self.post_order(root.rchild)
#             print(root.data, end=',')
#
#     # 情况一，node是叶子节点
#     def __remove_node_1(self, node):
#         if not node.parent:
#             self.root = None
#
#         if node == node.parent.lchild:  # node是他父亲的左孩子
#             node.parent.lchild = None
#             node.parent = None
#         else:  # 右孩子
#             node.parent.rchild = None
#
#     # 情况二，node是parent的只有一个右孩子
#     def __remove_node_22(self, node):
#         if not node.parent:  # 判断是否是根节点
#             self.root = node.rchild
#             node.rchild.parent = None
#         elif node == node.parent.lchild:  # l类似双向链表写法。画图可以理解,node节点是parent的左孩子且只有一个右孩子
#             node.parent.lchild = node.rchild
#             node.rchild.parent = node.parent
#         else:  # node节点是parent的右孩子且只有一个右孩子
#             node.parent.rchild = node.rchild
#             node.rchild.parent = node.parent
#
#     # 情况二，node是只有一个左孩子
#     def __remove_node_21(self, node):
#         if not node.parent:  # 判断是否是根节点
#             self.root = node.lchild
#             node.lchild.parent = None
#         elif node == node.parent.lchild:  # l类似双向链表写法。画图可以理解node节点是parent的左孩子且只有一个左孩子
#             node.parent.lchild = node.lchild
#             node.lchild.parent = node.parent
#         else: # node节点是parent的右孩子且只有一个左孩子
#             node.parent.rchild = node.lchild
#             node.lchild.parent = node.parent
#
#     # 数结构删除
#     def delete(self, val):
#         if self.root:   # 不是空树
#             node = self.query_no_rec(val)
#             if not node:  # 不存在
#                 return False
#             if not node.lchild and not node.rchild: # 叶子结点
#                 self.__remove_node_1(node)   # 两个下划线说明该函数是内部私有
#             elif not node.rchild:  # 一定只有一个左孩子
#                 self.__remove_node_21(node)
#             elif not node.lchild:  # 只要一个右孩子
#                 self.__remove_node_22(node)
#             else: # 两个孩子都有
#                 min_node = node.rchild
#                 while min_node.lchild:
#                     min_node = min_node.lchild
#                 node.data= min_node.data
#                 # 删除min_node
#                 if min_node.rchild:
#                     self.__remove_node_22(min_node)
#                 else:
#                     self.__remove_node_1(min_node)
#
#
# # tree = BST([1,4,2,5,3,8,6,9,7])
# # # tree.pre_order(tree.root)
# # # print("")
# # tree.in_order(tree.root)
# # print("")
# # tree.delete(4)
# # tree.delete(1)
# # tree.delete(8)
# # tree.in_order(tree.root)

"""
    标准案例
"""
# ! /usr/bin/env python
# -*- coding: utf-8 -*-
# Date: 2018/3/24

import random


class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None  # 左孩子
        self.rchild = None  # 右孩子
        self.parent = None


class BST:
    def __init__(self, li=None):
        self.root = None
        if li:
            for val in li:
                self.insert_no_rec(val)

    def insert(self, node, val):  # 插入操作，递归方式
        if not node:
            node = BiTreeNode(val)
        elif val < node.data:
            node.lchild = self.insert(node.lchild, val)
            node.lchild.parent = node
        elif val > node.data:
            node.rchild = self.insert(node.rchild, val)
            node.rchild.parent = node
        return node

    def insert_no_rec(self, val):
        p = self.root  # 头结点
        if not p:  # 空树
            self.root = BiTreeNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:  # 左子树存在
                    p = p.lchild
                else:  # 左孩子不存在
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p  # 主要是注意节点的返回情况
                    return
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
                    return
            else:
                return

    def query(self, node, val):
        if not node:
            return None
        if node.data < val:
            return self.query(node.rchild, val)
        elif node.data > val:
            return self.query(node.lchild, val)
        else:
            return node

    def query_no_rec(self, val):
        p = self.root
        while p:
            if p.data < val:
                p = p.rchild
            elif p.data > val:
                p = p.lchild
            else:
                return p
        return None

    # 先序遍历
    def pre_order(self, root):
        if root:
            print(root.data, end=',')
            self.pre_order(root.lchild)
            self.pre_order(root.rchild)

    # 中序遍历
    def in_order(self, root):
        if root:
            self.in_order(root.lchild)
            print(root.data, end=',')
            self.in_order(root.rchild)

    # 后序遍历
    def post_order(self, root):
        if root:
            self.post_order(root.lchild)
            self.post_order(root.rchild)
            print(root.data, end=',')

    def __remove_node_1(self, node):
        # 情况1：node是叶子节点
        if not node.parent:
            self.root = None
        if node == node.parent.lchild:  # node是它父亲的左孩子
            node.parent.lchild = None
        else:  # 右孩子
            node.parent.rchild = None

    def __remove_node_21(self, node):
        # 情况2.1：node只有一个左孩子
        if not node.parent:  # 根节点
            self.root = node.lchild
            node.lchild.parent = None
        elif node == node.parent.lchild:
            node.parent.lchild = node.lchild
            node.lchild.parent = node.parent
        else:
            node.parent.rchild = node.lchild
            node.lchild.parent = node.parent

    def __remove_node_22(self, node):
        # 情况2.2：node只有一个右孩子
        if not node.parent:
            self.root = node.rchild
        elif node == node.parent.lchild:
            node.parent.lchild = node.rchild
            node.rchild.parent = node.parent
        else:
            node.parent.rchild = node.rchild
            node.rchild.parent = node.parent

    def delete(self, val):
        if self.root:  # 不是空树
            node = self.query_no_rec(val)
            if not node:  # 不存在
                return False
            if not node.lchild and not node.rchild:  # 1. 叶子节点
                self.__remove_node_1(node)
            elif not node.rchild:  # 2.1 只有一个左孩子
                self.__remove_node_21(node)
            elif not node.lchild:  # 2.2 只有一个右孩子
                self.__remove_node_22(node)
            else:  # 3. 两个孩子都有
                min_node = node.rchild
                while min_node.lchild:
                    min_node = min_node.lchild
                node.data = min_node.data
                # 删除min_node
                if min_node.rchild:
                    self.__remove_node_22(min_node)
                else:
                    self.__remove_node_1(min_node)

#
#
# tree = BST([1,4,2,5,3,8,6,9,7])
# tree.in_order(tree.root)
# print("")
#
# tree.delete(4)
# tree.delete(1)
# tree.delete(8)
# tree.in_order(tree.root)
