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
        divisors = mapping.keys()

        for i in range(1,n+1):
            out_str = ""
            for key in divisors:
                if i%key == 0:
                    out_str += mapping[key]
            
            if len(out_str) == 0:
                out_str = str(i)

            out_lst.append(out_str)
        
        return out_lst

        
# @lc code=end

