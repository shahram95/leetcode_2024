#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x%10 == 0 and x!=0):
            return False
        
        temp = x
        inverted = 0

        while inverted < temp:
            inverted = inverted * 10 + temp%10
            temp //= 10
        
        return inverted == temp or inverted//10 == temp
        
# @lc code=end

