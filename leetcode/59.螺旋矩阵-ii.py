#
# @lc app=leetcode.cn id=59 lang=python
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        directionIndex = 0
        matrix = [[0]*n for _ in range(n)]
        row, column = 0, 0
        order = [i for i in range(1, n*n+1)]
        for i in order:
            matrix[row][column] = i
            nextRow = row + directions[directionIndex][0]
            nextColumn = column + directions[directionIndex][1]
            if not (0 <= nextRow < n and 0 <= nextColumn < n and matrix[nextRow][nextColumn] == 0):
                directionIndex = (directionIndex+1) % 4
            row += directions[directionIndex][0]
            column += directions[directionIndex][1]
        return matrix

# @lc code=end
