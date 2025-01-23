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
        total = rows * columns
        row, column = 0, 0
        visited = [[False] * columns for _ in range(rows)]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        directionIndex = 0
        orders = [0]*total

        for i in range(total):
            orders[i] = matrix[row][column]
            visited[row][column] = True
            nextRow = row + directions[directionIndex][0]
            nextColumn = column + directions[directionIndex][1]
            if not (0 <= nextRow < rows and 0 <= nextColumn < columns and not visited[nextRow][nextColumn]):
                directionIndex = (directionIndex+1) % 4
            row += directions[directionIndex][0]
            column += directions[directionIndex][1]
        return orders


# print("test")
# test = Solution()
# print(test.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
# @lc code=end
