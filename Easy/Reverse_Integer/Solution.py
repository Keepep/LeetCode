"""

Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21


Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1].
For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
"""

class Solution:
    def reverse(self, x: int) -> int:
        if -2**31>= x or x >= 2**31-1:
            return 0

        else:
            strX=str(x)
            if x >=0:
                result=strX[::-1]
            else:
                strX_wo_sign=strX[1:]
                result=strX[0]+strX_wo_sign[::-1]


        if -2**31>= int(result) or int(result) >= 2**31-1:
            return 0
        return int(result)