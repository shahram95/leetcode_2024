#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = x

        if num < 0 or (num%10 == 0 and num != 0):
            return False
        
        temp = 0

        while temp < num:
            temp = temp*10 + num%10
            num //= 10
        
        return temp == num or temp//10 == num
        
# @lc code=end

