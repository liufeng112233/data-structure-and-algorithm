# # -*- codeing = utf-8 -*-
# # @time :2023/2/16 10:37
# # @Project: data-structure-and-algorithm
# # @Author : 刘风
# # @File : AVL二叉数结构操作.py
# # @Software :PyCharm
# from 二叉树的遍历 import BiTreeNode, BST
#
#
# class AVLNode(BiTreeNode):
#     def __init__(self, data):
#         BiTreeNode.__init__(self, data)
#         self.bf = 0  # balance factor
#
#
# class AVLTree(BST):
#     def __init__(self, li=None):
#         BST.__init__(self, li)
#
#     def rotate_left(self, p, c):
#         s2 = c.lchild
#         p.rchild = s2
#         if s2:
#             s2.parent = p
#         c.lchild = p
#         p.parent = c
#         # 更新balance factor
#         p.bf = 0
#         c.bf = 0
#         return c
#
#     def rotate_right(self, p, c):  # 向右旋转
#         s2 = c.rchild
#         p.lchild = s2
#         if s2:
#             s2.parent = p
#         c.rchild = p
#         p.parent = c
#         p.bf = 0
#         c.bf = 0
#         return c
#
#     def rotate_right_left(self, p, c):
#         g = c.lchild
#
#         s3 = g.rchild
#         c.lchild = s3
#         if s3:
#             s3.parent = c
#         g.rchild = c
#         c.parent = g
#
#         s2 = g.lchild
#         p.rchild = s2
#         if s2:
#             s2.parent = p
#         g.rechild = p
#         p.parent = g
#
#         # 更新bf
#         if g.bf > 0:
#             p.bf = -1
#             c.bf = 0
#         elif g.bf < 0:
#             p.bf = 0
#             c.bf = 1
#         else:
#             # s空，插入的g
#             p.bf = 0
#             c.bf = 0
#         return g
#
#     def rotate_left_right(self, p, c):
#         g = c.rchild
#
#         s2 = g.lchild
#         c.rchild = s2
#         if s2:
#             s2.parent = c
#
#         g.lchild = c
#         c.parent = g
#
#         s3 = g.rchild
#         p.rchild = s3
#         if s3:
#             s3.parent = p
#         g.rchild = p
#         p.parent = g
#
#         # 更新
#         if g.bf < 0:  # 说明器等于1
#             p.bf = 1
#             c.bf = 0
#         elif g.bf > 0:
#             p.bf = 0
#             c.bf = -1
#         else:
#             p.bf = 0
#             c.bf = 0
#         return g
#
#     def insert_not_rec(self, val):
#         # 和BST一样，需要插入
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
#                     p.lchild.parent = p  # 存储插入的节点
#                     node = p.lchild
#                     break
#             elif val > p.data:
#                 if p.rchild:
#                     p = p.rchild
#                 else:
#                     p.rchild = BiTreeNode(val)
#                     p.rchild.parent = p
#                     node = p.rchild
#                     break
#             else:  # val==p.data
#                 return
#         # 更新bf
#         while node.parent:  # node.parent 不空
#             if node.parent.lchild == node:
#                 # 更新node.parent的bf -1
#                 if node.parent.bf < 0:  # 原来node.parent.bf==-1，更新后变成-2
#                     # 看node的哪边沉
#                     g = node.parent.parent  # 为连接旋之后的子树
#                     if node.bf > 0:
#                         n = self.rotate_left_right(node.parent, node)
#                     else:
#                         n = self.rotate_right(node.parent, node)
#                     # 记得将n和g连接起来
#                 elif node.parent.bf > 0:  # 原来mode.parent.bf=1，更新后变成0
#                     node.parent.bf = 0
#                     break
#                 else:  # 原来node.parent.bf=0，更新后变成-1
#                     node.parent.bf = -1
#                     node = node.parent
#                     continue
#             else:  # 传递四从右子树来的，右子树更沉
#                 # 更新后的node.parent.bf+=1
#                 if node.parent.bf > 0:  # 原来的node.parent.bf==1现在变成2
#                     # 做旋转
#                     # 看node哪边沉
#                     g = node.parent.parent
#                     if node.bf < 0:  # node.bf =1
#                         n = self.rotate_right_left(node.parent, node)
#                     else:  # node.bf=-1
#                         n = self.rotate_left(node.parent, node)
#                     # 记得连起来
#                 elif node.parent.bf < 0:  # -1--->0
#                     node.parent.bf = 0
#                     break
#                 else:  # 0--->1
#                     node.parent.bf = 1
#                     node = node.parent
#                     continue
#             # 链接旋转后的子树
#             n.parent = g
#
#             if g:  # 判断g是否存在，非空
#                 if node.parent == g.lchild:
#                     g.lchild = n
#                 else:
#                     g.rchild = n
#                     break
#
#                 pass
#             else:
#                 self.root = n
#                 break
#
# # 测试
# tree =AVLTree([9,8,7,6,5,4,3,2,1])

"""
    标准案例
"""
from 二叉树的遍历 import BiTreeNode, BST

class AVLNode(BiTreeNode):
    def __init__(self, data):
        BiTreeNode.__init__(self, data)
        self.bf = 0

class AVLTree(BST):
    def __init__(self, li=None):
        BST.__init__(self, li)

    def rotate_left(self, p, c):
        s2 = c.lchild
        p.rchild = s2
        if s2:
            s2.parent = p

        c.lchild = p
        p.parent = c

        p.bf = 0
        c.bf = 0
        return c

    def rotate_right(self, p, c):
        s2 = c.rchild
        p.lchild = s2
        if s2:
            s2.parent = p

        c.rchild = p
        p.parent = c

        p.bf = 0
        c.bf = 0
        return c

    def rotate_right_left(self, p, c):
        g = c.lchild

        s3 = g.rchild
        c.lchild = s3
        if s3:
            s3.parent = c
        g.rchild = c
        c.parent = g

        s2 = g.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        g.lchild = p
        p.parent = g

        # 更新bf
        if g.bf > 0:
            p.bf = -1
            c.bf = 0
        elif g.bf < 0:
            p.bf = 0
            c.bf = 1
        else: # 插入的是g
            p.bf = 0
            c.bf = 0
        return g

    def rotate_left_right(self, p, c):
        g = c.rchild

        s2 = g.lchild
        c.rchild = s2
        if s2:
            s2.parent = c
        g.lchild = c
        c.parent = g

        s3 = g.rchild
        p.lchild = s3
        if s3:
            s3.parent = p
        g.rchild = p
        p.parent = g

        # 更新bf
        if g.bf < 0:
            p.bf = 1
            c.bf = 0
        elif g.bf > 0:
            p.bf = 0
            c.bf = -1
        else:
            p.bf = 0
            c.bf = 0
        return g



    def insert_no_rec(self, val):
        # 1. 和BST一样，插入
        p = self.root
        if not p:  # 空树
            self.root = AVLNode(val)
            return
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:  # 左孩子不存在
                    p.lchild = AVLNode(val)
                    p.lchild.parent = p
                    node = p.lchild # node 存储的就是插入的节点
                    break
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = AVLNode(val)
                    p.rchild.parent = p
                    node = p.rchild
                    break
            else:   # val == p.data
                return

        # 2. 更新balance factor
        while node.parent:  # node.parent不空
            if node.parent.lchild == node: # 传递是从左子树来的，左子树更沉了
                #更新node.parent的bf -= 1
                if node.parent.bf < 0: # 原来node.parent.bf == -1, 更新后变成-2
                    # 做旋转
                    # 看node哪边沉
                    g = node.parent.parent # 为了连接旋转之后的子树
                    x = node.parent  # 旋转前的子树的根
                    if node.bf > 0:
                        n = self.rotate_left_right(node.parent, node)
                    else:
                        n = self.rotate_right(node.parent, node)
                    # 记得：把n和g连起来
                elif node.parent.bf > 0: # 原来node.parent.bf = 1，更新之后变成0
                    node.parent.bf = 0
                    break
                else: # 原来node.parent.bf = 0，更新之后变成-1
                    node.parent.bf = -1
                    node = node.parent
                    continue
            else: # 传递是从右子树来的，右子树更沉了
                #更新node.parent.bf += 1
                if node.parent.bf > 0:  # 原来node.parent.bf == 1, 更新后变成2
                    # 做旋转
                    # 看node哪边沉
                    g = node.parent.parent # 为了连接旋转之后的子树
                    x = node.parent  # 旋转前的子树的根
                    if node.bf < 0: # node.bf = 1
                        n = self.rotate_right_left(node.parent, node)
                    else:   # node.bf = -1
                        n = self.rotate_left(node.parent, node)
                    # 记得连起来
                elif node.parent.bf < 0: # 原来node.parent.bf = -1，更新之后变成0
                    node.parent.bf = 0
                    break
                else: # 原来node.parent.bf = 0，更新之后变成1
                    node.parent.bf = 1
                    node = node.parent
                    continue

            # 链接旋转后的子树
            n.parent = g
            if g: # g不是空
                if x == g.lchild:
                    g.lchild = n
                else:
                    g.rchild = n
                break
            else:
                self.root = n
                break


tree = AVLTree([9,8,7,6,5,4,3,2,1])

tree.pre_order(tree.root)
print("")
tree.in_order(tree.root)
