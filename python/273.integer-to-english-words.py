#
# @lc app=leetcode id=273 lang=python3
#
# [273] Integer to English Words
#

# @lc code=start
class Solution:
    def numberToWords(self, num: int) -> str:

        if num == 0:
            return "Zero"

        ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
        tens = ["", "", "Twenty", "Thirty", "Forty", "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
        thousands = ["", "Thousand", "Million", "Billion"]

        def threeDigitToWord(n : int) -> str:
            if n == 0:
                return "Zero"
            
            elif n < 20:
                return ones[n]
            elif n < 100:
                return tens[n//10] + (" " + ones[n%10] if n%10 != 0 else "")
            else:
                return ones[n//100] + " Hundred" + (" " + threeDigitToWord(n%100) if n%100 != 0 else "")
        
        result = []
        group = 0

        while num > 0:
            current_chunk = num % 1000
            if current_chunk != 0:
                words = threeDigitToWord(current_chunk)
                if thousands[group]:
                    words += " " + thousands[group]
                result.append(words)
            group += 1
            num //= 1000
        
        final_result = " ".join(result[::-1]).strip()
        return final_result

        
# @lc code=end

