#
# @lc app=leetcode.cn id=289 lang=python
#
# [289] 生命游戏
#

# @lc code=start
class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        rows = len(board)
        columns = len(board[0])
        board_cp = [[board[row][column]
                     for column in range(columns)] for row in range(rows)]
        neighbors = [(1, 0), (1, -1), (0, -1), (-1, -1),
                     (-1, 0), (-1, 1), (0, 1), (1, 1)]
        for row in range(rows):
            for column in range(columns):
                liveNeighbors = 0
                for neighbor in neighbors:
                    r = row + neighbor[0]
                    c = column + neighbor[1]
                    if (0 <= r < rows and 0 <= c < columns and board_cp[r][c] == 1):
                        liveNeighbors += 1
                if liveNeighbors < 2:
                    board[row][column] = 0
                elif liveNeighbors == 2:
                    board[row][column] = board_cp[row][column]
                elif liveNeighbors == 3:
                    board[row][column] = 1
                else:
                    board[row][column] = 0


# @lc code=end
