#
# @lc app=leetcode id=408 lang=python3
#
# [408] Valid Word Abbreviation
#

# @lc code=start
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_idx = 0
        abbr_idx = 0

        while word_idx < len(word) and abbr_idx < len(abbr):
            if abbr[abbr_idx].isdigit():
                if abbr[abbr_idx] == '0':
                    return False
                num = 0

                while abbr_idx < len(abbr) and abbr[abbr_idx].isdigit():
                    num = num*10 + int(abbr[abbr_idx])
                    abbr_idx += 1
                
                word_idx += num
            else:
                if word_idx > len(word) or word[word_idx] != abbr[abbr_idx]:
                    return False
                
                word_idx += 1
                abbr_idx += 1
        
        return word_idx == len(word) and abbr_idx == len(abbr)
# @lc code=end

