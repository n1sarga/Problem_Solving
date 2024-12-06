'''Problem Link: https://leetcode.com/problems/reverse-integer/description/'''

class Solution:
    def reverse (self, x: int) -> int:
        
        if x < 0:
            x_abs = abs(x)
            x_str = str(x_abs)
            x_str = ''.join(reversed(x_str))
            x_int = int(x_str) * -1
        else:
            x_str = str(x)
            x_str = ''.join(reversed(x_str))
            x_int = int(x_str)

        if x_int > 2**31 - 1 or x_int < -2**31:
            return 0
        
        return x_int