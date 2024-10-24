#
# @lc app=leetcode id=1550 lang=python3
#
# [1550] Three Consecutive Odds
#

# @lc code=start
import math

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        lp = 0
        rp = 3

        while rp <= len(arr):
            if math.prod(arr[lp:rp])%2:
                return True
            lp += 1
            rp += 1
        
        return False
        
# @lc code=end

