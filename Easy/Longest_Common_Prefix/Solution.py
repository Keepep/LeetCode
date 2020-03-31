"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""



class Solution:
     def longestCommonPrefix(self, strs) -> str:
            if not strs:
                return ""
            if len(strs) == 1:
                return strs[0]
            result=""
            minSize = min([len(x) for x in strs])
            pointer = 0
            while (pointer < minSize):
                if len({s[pointer] for s in strs}) == 1:
                    result += strs[0][pointer]
                    pointer+=1
                else:
                    break
            return result

