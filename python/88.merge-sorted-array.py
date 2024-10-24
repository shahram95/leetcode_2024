#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        lp = m-1
        rp = n-1

        for idx in range(m+n-1, -1, -1):
            if rp < 0:
                break

            if lp >= 0 and nums1[lp] > nums2[rp]:
                nums1[idx] = nums1[lp]
                lp -= 1
            else:
                nums1[idx] = nums2[rp]
                rp -= 1
            
        
# @lc code=end

