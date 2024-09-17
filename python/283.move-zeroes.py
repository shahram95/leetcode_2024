#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#

# @lc code=start
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        scanIdx = 0
        currIdx = 0

        while scanIdx < len(nums):
            if nums[currIdx] == 0:
                nums.append(nums.pop(currIdx))
            else:
                currIdx += 1
            scanIdx += 1
            
        
# @lc code=end

