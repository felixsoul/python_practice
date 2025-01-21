#
# @lc app=leetcode.cn id=48 lang=python
#
# [48] 旋转图像
#

# @lc code=start
class Solution(object):
    def rotate(self, matrix):
        tmp = 0
        n = len(matrix)
        matrix_new = [[0 for _ in range(n)] for _ in range(n)]

        for i in range(n):
            for j in range(n):
                matrix_new[j][n-i-1] = matrix[i][j]
        matrix[:] = matrix_new
        return matrix


# @lc code=end
