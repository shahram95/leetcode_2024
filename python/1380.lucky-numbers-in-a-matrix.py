#
# @lc app=leetcode id=1380 lang=python3
#
# [1380] Lucky Numbers in a Matrix
#

# @lc code=start
class Solution:
    def luckyNumbers(self, matrix: List[List[int]]) -> List[int]:
        min_row = {min(matrix[i]) for i in range(len(matrix))}
        max_col = {(max(matrix[i][j] for i in range(len(matrix)))) for j in range(len(matrix[0]))}
        return list(min_row&max_col)
# @lc code=end

