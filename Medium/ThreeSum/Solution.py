"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


class Solution:

    def threeSum(self, nums):
        # (i) remove duplicated cases
        result = set()
        nums = sorted(nums)

        for i in range(len(nums)):
            # can't make triplet solution in this case
            if nums[i] > 0: break

            # (ii) remove duplicated cases
            if i > 0 and nums[i] == nums[i - 1]: continue

            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum > 0:
                    right -= 1
                elif sum < 0:
                    left += 1
                else:
                    result.add((nums[i], nums[left], nums[right]))

                    # process continously to find another possible solution for "i"
                    left += 1
                    right -= 1
        return list(result)