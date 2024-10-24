#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#

# @lc code=start
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        mapping = {
            3 : "Fizz",
            5 : "Buzz"
        }
        out_lst = list()

        for i in range(1,n+1):
            curr_str = ""

            for key in mapping.keys():
                if i%key == 0:
                    curr_str += mapping[key]
            
            curr_str += str(i) if len(curr_str) == 0 else ""
            out_lst.append(curr_str)
        
        return out_lst
# @lc code=end

