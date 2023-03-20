# -*- codeing = utf-8 -*-
# @time :2023/2/14 11:02
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 二叉树.py
# @Software :PyCharm
# 二叉树的链式存储结构，可以递归定义的数据结构
class Node:
    def __init__(self, name, type='dir'):
        self.name = name
        self.type = type
        self.children = []  # 建立关联
        self.parent = None  # 反向连接

    def __repr__(self):  # 定义对象的文本叙述
        return self.name


class FileSystemTree:
    def __init__(self):
        self.root = Node("/")
        self.now = self.root

    def mkdir(self, name):
        if name[-1] != "/":  # name判断是否是“/”结尾
            name += "/"
        node = Node(name)
        self.now.children.append(node)
        node.parent = self.now

    def ls(self):  # 展示当前目录下的全部目录
        return self.now.children

    def cd(self, name):  # 切换目录
        if name[-1] != "/":  # 判断结尾条件
            name += "/"
        for child in self.now.children:
            if child.name ==name:
                self.now = child
        raise ValueError("invalid dir")



Tree = FileSystemTree()
Tree.mkdir("var/")
Tree.mkdir("bin/")
Tree.mkdir("usr/")

Tree.cd("bin/")
Tree.mkdir("python/")
print(Tree.ls())

# n = Node("hello")
# n2 = Node("world")
# n.children.append(n2)
# n2.parent = n


"""
    二叉树的遍历
"""
# 前序遍历