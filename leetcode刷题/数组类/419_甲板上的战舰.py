class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        board = [["X", ".", ".", "X"], [".", ".", ".", "X"], [".", ".", ".", "X"]]
        ans = 0
        m, n = len(board), len(board[0])  # 行列数
        for i, row in enumerate(board):  # 遍历某一行
            for j, ch in enumerate(row):
                if ch == 'X':
                    row[j] = '.'
                    for k in range(j + 1, n):  # 遍历本行后面有无战舰，处理同行
                        if row[k] != 'X':
                            break
                        row[k] = '.'   #满足board[i][j]是战舰时，同行同列应该是'.'
                    for k in range(i + 1, m):  # 遍历下面有无战舰,处理同列
                        if board[k][j] != 'X':
                            break
                        board[k][j] = '.'   #满足board[i][j]是战舰时，同行同列应该是'.'
                    ans += 1
        return ans