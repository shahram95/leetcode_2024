#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        out_str = ""

        for idx in range(len(strs[0])):
            if strs[0][idx] == strs[-1][idx]:
                out_str += strs[0][idx]
            else:
                break
        
        return out_str
        
# @lc code=end

