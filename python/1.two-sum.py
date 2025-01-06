#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Method # 1: Brute Force
        '''
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == target - nums[j]:
        #             return [i,j]
        # return []

        '''
        Method # 2: Two pass hashtable
        '''
        # hashmap = dict()

        # for i in range(len(nums)):
        #     hashmap[nums[i]] = i
        # for i in range(len(nums)):
        #     comp = target - nums[i]
        #     if comp in hashmap and hashmap[comp] != i:
        #         return [hashmap[comp], i]
        # return []

        '''
        Method # 3: One pass hashtable
        '''
        idx_dict = dict()

        for idx,num in enumerate(nums):
            comp = target - num
            if comp in idx_dict:
                return [idx_dict[comp], idx]
            idx_dict[num] = idx
        return []
# @lc code=end

