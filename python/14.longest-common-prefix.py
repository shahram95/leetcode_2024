#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        out = ""

        for idx in range(len(strs[0])):
            if strs[0][idx] != strs[-1][idx]:
                break
            out += strs[0][idx]
        
        return out
# @lc code=end

