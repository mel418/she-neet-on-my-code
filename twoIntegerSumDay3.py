'''
Two Integer Sum
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:
Input: 
nums = [3,4,5,6], target = 7
Output: [0,1]
Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:
Input: nums = [4,5,6], target = 10
Output: [0,2]

Example 3:
Input: nums = [5,5], target = 10
Output: [0,1]

Constraints:
2 <= nums.length <= 1000
-10,000,000 <= nums[i] <= 10,000,000
-10,000,000 <= target <= 10,000,000
'''
from typing import List

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    # Dictionary to record the indices of the numbers we've passed through
    seen = {}  
    for i, num in enumerate(nums):
      complement = target - num  # Calculate the complement (the number needed to reach the target sum)
      
      if complement in seen:  # If the complement is already in the dictionary, return the pair of indices
        return [seen[complement], i]
      
      seen[num] = i  # Store the index of the current number


solution = Solution()
print(solution.twoSum([3, 4, 5, 6], 7))  # Output: [0, 1]
print(solution.twoSum([4, 5, 6], 10))    # Output: [0, 2]
print(solution.twoSum([5, 5], 10))       # Output: [0, 1]

