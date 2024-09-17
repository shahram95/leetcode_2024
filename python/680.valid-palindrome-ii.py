#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#

# @lc code=start
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def checkPalindrome(s, lp, rp):
            while lp<rp:
                if s[lp] != s[rp]:
                    return False
                lp += 1
                rp -= 1
            return True
        lp = 0
        rp = len(s)-1

        while lp < rp:
            if s[lp] != s[rp]:
                return checkPalindrome(s, lp+1, rp) or checkPalindrome(s, lp, rp-1)
            lp += 1
            rp -= 1

        return True       
# @lc code=end

