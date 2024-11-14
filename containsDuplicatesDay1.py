'''
Duplicate Integer

Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1
Input: nums = [1, 2, 3, 3]
Output: true

Example 2:
Input: nums = [1, 2, 3, 4]
Output: false
'''
from typing import List

class Solution:
  def hasDuplicate(self, nums: List[int]) -> bool:
    unique = set(nums)
    # print(unique)
    if len(unique) == len(nums):
        return False
    else:
        return True

nums1 = [1, 2, 3, 3]
nums2 = [1, 2, 3, 4]

solution = Solution()
print(solution.hasDuplicate(nums1))  # Output: True
print(solution.hasDuplicate(nums2))          # Output: False

