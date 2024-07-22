#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        mapping = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        sum = 0
        idx = 0

        while idx < len(s):
            if idx+1 < len(s) and mapping[s[idx]] < mapping[s[idx+1]]:
                sum += (mapping[s[idx+1]]-mapping[s[idx]])
                idx += 2
            else:
                sum += mapping[s[idx]]
                idx += 1
        
        return sum
        
# @lc code=end

