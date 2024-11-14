'''
Is Anagram

Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: s = "racecar", t = "carrace"
Output: true

Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

s and t consist of lowercase English letters.
'''

class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    if len(s)!=len(t):
      return False
    count = {}

    for char in (s):
      count[char] = count.get(char,0)+1
    for char in t:
      if count.get(char) is None:
        return False
      count[char] -= 1
      if count[char] < 0:
        return False
    # print(count.values())
    return all(value== 0 for value in count.values())
            
solution = Solution()
print(solution.isAnagram("racecar", "carrace"))  # Output: True
print(solution.isAnagram("jar", "jam"))          # Output: False
