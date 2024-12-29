#
# @lc app=leetcode id=1701 lang=python3
#
# [1701] Average Waiting Time
#

# @lc code=start
class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        net_wait_time = 0
        next_idle_time = 0

        for customer in customers:
            next_idle_time = max(next_idle_time, customer[0]) + customer[1]
            net_wait_time += next_idle_time - customer[0]
        average_wait_time = net_wait_time/len(customers)
        return average_wait_time
# @lc code=end

