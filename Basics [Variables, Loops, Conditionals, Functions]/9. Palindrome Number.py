'''Problem Link: https://leetcode.com/problems/palindrome-number/description/'''

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        y = str(x)
        z = ''.join(reversed(y))
        if y == z:
            return True
        else:
            return False