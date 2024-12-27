#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#

# @lc code=start
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        remove_idx = set()
        stack = list()

        for i,c in enumerate(s):
            if c not in '()':
                continue
            if c == '(':
                stack.append(i)
            elif not stack:
                remove_idx.add(i)
            else:
                stack.pop()
        
        remove_idx = remove_idx.union(set(stack))
        string_builder = ''

        for i,c in enumerate(s):
            if i not in remove_idx:
                string_builder += s[i]
        return string_builder
# @lc code=end

