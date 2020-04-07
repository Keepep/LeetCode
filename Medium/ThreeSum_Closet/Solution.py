"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to target. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        result = target + 10000000
        for i in range(len(nums) - 1):
            #skip duplicate cases
            if i > 0 and nums[i - 1] == nums[i]: continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
                elif sum == target:
                    return target

                #if sum value is closer to target than result value
                if abs(target - sum) <= abs(target - result):
                    result = sum
        return result