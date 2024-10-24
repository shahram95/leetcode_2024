#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        sqrt5 = sqrt(5)
        phi = (1+sqrt5)/2
        psi = (1-sqrt5)/2
        count = ((phi)**(n+1) - (psi)**(n+1))/sqrt5
        return int(count)
        
# @lc code=end

