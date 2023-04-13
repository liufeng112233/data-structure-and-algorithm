# -*- codeing = utf-8 -*-
# @time :2023/4/5 20:59
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 114_二叉树展开为链表.py
# @Software :PyCharm
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#

class Solution(object):
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        list1 = list()  # 构建空链表存储数据

        # 采用递归方式
        def root_append(root):  # 先序遍历，先根节点，左孩子，右孩子
            if root:
                list1.append(root)
                root_append(root.left)  # 直接处理根节点
                root_append(root.right)

        root_append(root)
        size = len(list1)
        for i in range(1, size):
            prev, curr = list1[i - 1], list1[i]
            prev.left = None
            prev.right = curr
