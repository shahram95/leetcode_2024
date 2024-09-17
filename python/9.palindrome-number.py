#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
<<<<<<< HEAD
        if x < 0 or (x%10 == 0 and x!=0):
            return False

        temp = x
        invert = 0

        while temp > invert:
            invert = invert*10 + temp%10
            temp //= 10
        
        return invert == temp or invert//10 == temp
=======
        num = x

        if num < 0 or (num%10 == 0 and num != 0):
            return False
        
        temp = 0

        while temp < num:
            temp = temp*10 + num%10
            num //= 10
        
        return temp == num or temp//10 == num
>>>>>>> july_24_branch
        
# @lc code=end

