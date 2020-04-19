"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

class Solution:
    def generateParenthesis(self, n: int):

        result=list('(')


        while len(result[0])< n*2:
            tmpResult=list()
            for i in range(len(result)):
                lb_num=result[i].count('(')
                rb_num=result[i].count(')')

                if lb_num > rb_num:
                    tmpResult.append(result[i]+')')
                if lb_num < n:
                    tmpResult.append(result[i] + '(')
            result=tmpResult
        return result