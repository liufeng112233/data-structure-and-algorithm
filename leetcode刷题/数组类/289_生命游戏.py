# -*- codeing = utf-8 -*-
# @time :2023/3/24 19:55
# @Project: data-structure-and-algorithm
# @Author : 刘风
# @File : 289_生命游戏.py
# @Software :PyCharm
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # board = [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
        board = [[1, 1], [1, 0]]
        neighbors = [[-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1], [0, -1]]
        m, n = len(board), len(board[0])
        dic0 = []  # 保存原始数据中的0
        dic1 = []  # 保存原始数据中的1
        for i in range(m):
            for j in range(n):
                if board[i][j] == 0:
                    dic0.append([i, j])
                elif board[i][j] == 1:
                    dic1.append([i, j])

        for c in dic0:  # 统计0周围有多少个1
            flag_1 = 0  # 统计1的个数
            for k in range(8):
                cc = [c[0] + neighbors[k][0], c[1] + neighbors[k][1]]
                if cc in dic1:   # 死细胞是根据活细胞进行判断
                    flag_1 += 1
            if flag_1 == 3:
                board[c[0]][c[1]] = 1

        for b in dic1:  # 对活细胞处理
            flag_0 = 0
            for k in range(8):
                bb = [b[0] + neighbors[k][0], b[1] + neighbors[k][1]]
                if bb in dic1:   # 或心包是根据或周围或活细胞的数量来判断其生存关系
                    flag_0 += 1
            if flag_0 < 2 or flag_0 > 3:
                board[b[0]][b[1]] = 0
            elif flag_0 == 2 or flag_0 == 3:
                board[b[0]][b[1]] = 1
        return board
