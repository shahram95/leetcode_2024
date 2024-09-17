#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        out_str = ""
        counter = min(len(word1), len(word2))

        for idx in range(counter):
            out_str += word1[idx]
            out_str += word2[idx]
        
        return out_str + word1[counter:] + word2[counter:]
# @lc code=end

