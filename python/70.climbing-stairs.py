#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#
from math import sqrt

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        sqrt5 = sqrt(5)
        phi = (1+sqrt5)/2
        psi = (1-sqrt5)/2
        count = int((phi**(n+1) - psi**(n+1))//sqrt5)
        return count
        
# @lc code=end

