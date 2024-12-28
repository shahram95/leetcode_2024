#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(lp,rp):
            return s[lp:rp][::-1] == s[lp:rp]

        lp = 0
        rp = len(s)-1

        while lp<rp:
            if s[lp] != s[rp]:
                return checkPalindrome(lp+1, rp+1) or checkPalindrome(lp, rp)
            lp += 1
            rp -= 1
        return True
# @lc code=end

