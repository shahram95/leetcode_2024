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
        scannedIdx = 0
        currIdx = 0

        while scannedIdx < len(nums):
            if nums[currIdx] != 0:
                currIdx += 1
            else:
                nums.append(nums.pop(currIdx))
        
            scannedIdx += 1
        
# @lc code=end

