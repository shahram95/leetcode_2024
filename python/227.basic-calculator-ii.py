#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#

# @lc code=start
class Solution:
    def calculate(self, s: str) -> int:
        if not s:
            return 0
        
        current_number = 0
        last_number = 0
        result = 0
        sign = '+'

        for i in range(len(s)):
            current_char = s[i]

            if current_char.isdigit():
                current_number = current_number*10 + int(current_char)
            if (not current_char.isdigit()) and not current_char.isspace() or i == len(s)-1:
                if sign == '+' or sign == '-':
                    result += last_number
                    last_number = current_number if sign == '+' else -current_number
                elif sign == '*':
                    last_number = last_number*current_number
                elif sign == '/':
                    last_number = int(last_number/current_number)
                
                current_number = 0
                sign = current_char
        result += last_number
        return result
# @lc code=end

