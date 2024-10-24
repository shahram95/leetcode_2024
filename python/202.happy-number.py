#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#

# @lc code=start
class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number):
            total = 0

            while number>0:
                number,digit = divmod(number,10)
                total += digit**2
            
            return total

        slow_runner = n
        fast_runner = get_next(n)

        while fast_runner != 1 and fast_runner != slow_runner:
            slow_runner = get_next(slow_runner)
            fast_runner = get_next(get_next(fast_runner))
        
        return fast_runner == 1
        
# @lc code=end

