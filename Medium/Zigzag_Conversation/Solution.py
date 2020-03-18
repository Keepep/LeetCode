"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
Example 1:

Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"
Example 2:

Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:

P     I    N
A   L S  I G
Y A   H R
P     I

"""

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        size=len(s)

        if numRows <=1:
            return s
        else:
            interval=numRows-2

        iter=interval+numRows
        result=list()
        for i in range(numRows):
            for j in range(i,size,iter):
                result.append(s[j])
                if i!=0 and i!=numRows-1 and iter+j-2*i < size:
                    result.append(s[iter+j-2*i])


        return ''.join(result)