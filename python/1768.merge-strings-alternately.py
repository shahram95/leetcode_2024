#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        itr = min(len(word1), len(word2))
        out  = ""

        for idx in range(itr):
            out += (word1[idx] + word2[idx])
        
        return out + word1[itr:] + word2[itr:]
        
# @lc code=end

