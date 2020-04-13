"""
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]
"""


class Solution:
    def fourSum(self, nums, target: int):
        nums.sort()
        print(nums)
        result=set()
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                if i > 0 and nums[i] == nums[i - 1]: continue
                if j > 0 and nums[j] == nums[j - 1]: continue
                left=j+1
                right=len(nums)-1

                while left< right:
                    sum = nums[i] + nums[j] + nums[left] + nums[right]

                    if target > sum:
                        left+=1
                    elif target < sum:
                        right-=1
                    else:
                        result.add((nums[i],nums[j],nums[left],nums[right]))
                        left+=1
                        right-=1

        return list(result)

