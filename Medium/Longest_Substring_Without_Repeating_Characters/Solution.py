"""
Given a string, find the length of the longest substring without repeating characters.
######
Example 1
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
######
Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result=0
        dict={}
        start=0
        for index, value  in enumerate(s):
            if dict.get(value)!=None:
                tmpStart=dict[value]+1
                if tmpStart> start:
                    start=tmpStart
            tmpResult=index-start+1
            if tmpResult >result:
                result=tmpResult
            dict[value]=index

        return result