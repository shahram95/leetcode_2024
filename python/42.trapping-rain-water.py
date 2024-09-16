#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 3:
            return 0
        
        left, right = 0, len(height)-1
        leftmax, rightmax = height[left], height[right]
        ans = 0

        while left < right:
            if height[left] < height[right]:
                if height[left] > leftmax:
                    leftmax = height[left]
                else:
                    ans += leftmax - height[left]
                left += 1
            else:
                if height[right] > rightmax:
                    rightmax = height[right]
                else:
                    ans += rightmax - height[right]
                right -= 1
        return ans

        
# @lc code=end

