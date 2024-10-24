#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(s):
            return s == s[::-1]
        
        lp = 0
        rp = len(s)-1

        while lp<rp:
            if s[lp] == s[rp]:
                lp += 1
                rp -= 1
            else:
                return checkPalindrome(s[lp:rp]) or checkPalindrome(s[lp+1:rp+1])
        
        return True
# @lc code=end

