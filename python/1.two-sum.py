#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_dict = dict()

        for idx, num in enumerate(nums):
            comp = target - num
            if comp in idx_dict:
                return [idx_dict[comp], idx]
            else:
                idx_dict[num] = idx
        
        return []
# @lc code=end

