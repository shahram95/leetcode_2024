#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()

        mapping = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for c in s:
            if c in mapping:
                last_element = stack.pop() if len(stack) else "#"
                if last_element != mapping[c]:
                    return False
            else:
                stack.append(c)
        
        return len(stack) == 0
# @lc code=end

