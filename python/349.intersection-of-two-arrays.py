#
# @lc app=leetcode id=349 lang=python3
#
# [349] Intersection of Two Arrays
#

# @lc code=start
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        def calIntersection(nums1, nums2):
            return [x for x in nums1 if x in nums2]

        nums1 = set(nums1)
        nums2 = set(nums2)

        if len(nums1) > len(nums2):
            inter = calIntersection(nums1,nums2)
        else:
            inter = calIntersection(nums2, nums1)
        
        return inter
# @lc code=end

