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
<<<<<<< HEAD
=======

>>>>>>> july_24_branch
        p1 = m - 1
        p2 = n - 1
        
        for idx in range(m+n-1, -1, -1):
            if p2 < 0:
                break
<<<<<<< HEAD
            elif p1 >= 0 and nums1[p1] > nums2[p2]:
=======
            if p1 >= 0 and nums1[p1] > nums2[p2]:
>>>>>>> july_24_branch
                nums1[idx] = nums1[p1]
                p1 -= 1
            else:
                nums1[idx] = nums2[p2]
                p2 -= 1
<<<<<<< HEAD
                
=======

>>>>>>> july_24_branch
        
# @lc code=end

