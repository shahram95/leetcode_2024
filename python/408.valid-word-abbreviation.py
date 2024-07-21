#
# @lc app=leetcode id=408 lang=python3
#
# [408] Valid Word Abbreviation
#

# @lc code=start
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        word_pointer = 0
        abbr_pointer = 0

        while word_pointer < len(word) and abbr_pointer < len(abbr):
            if abbr[abbr_pointer].isdigit():
                if abbr[abbr_pointer] == '0':
                    return False
                
                num = 0

                while abbr_pointer < len(abbr) and abbr[abbr_pointer].isdigit():
                    num = num*10 + int(abbr[abbr_pointer])
                    abbr_pointer += 1
                word_pointer += num
            
            else:
                if word_pointer >= len(word) or word[word_pointer] != abbr[abbr_pointer]:
                    return False
                word_pointer += 1
                abbr_pointer += 1
        return len(abbr) == abbr_pointer and len(word) == word_pointer

# @lc code=end

