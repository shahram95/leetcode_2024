#
# @lc app=leetcode id=1768 lang=python3
#
# [1768] Merge Strings Alternately
#

# @lc code=start
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        minLen = min(len(word1), len(word2))
        out = ''

        for idx in range(minLen):
            out += (word1[idx]+ word2[idx])
        return out + word1[minLen:] + word2[minLen:]
# @lc code=end

