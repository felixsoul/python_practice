#
# @lc app=leetcode.cn id=54 lang=python
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        rows = len(matrix)
        columns = len(matrix[0])
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        total = rows*columns
        order = [0]*total
        visited = [[False]*columns for _ in range(rows)]

        directionIndex = 0
        row, column = 0, 0

        for i in range(total):
            order[i] = matrix[row][column]
            visited[row][column] = True
            nextRow, nextColumn = row + \
                directions[directionIndex][0], column + \
                directions[directionIndex][1]
            if not (0 <= nextRow < rows and 0 <= nextColumn < columns and not visited[nextRow][nextColumn]):
                directionIndex = (directionIndex+1) % 4
            row += directions[directionIndex][0]
            column += directions[directionIndex][1]
        return order


# @lc code=end
