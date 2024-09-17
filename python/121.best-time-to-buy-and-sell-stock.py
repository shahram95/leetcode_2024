#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = float('inf')
        maxprofit = 0

        for price in prices:
            if price < minprice:
                minprice = price
            elif maxprofit < price - minprice:
                maxprofit = price - minprice
        
        return maxprofit
        
# @lc code=end

