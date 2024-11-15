'''
Anagram Groups
Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:
Input: strs = ["x"]
Output: [["x"]]

Example 3:
Input: strs = [""]
Output: [[""]]

Constraints:
1 <= strs.length <= 1000.
0 <= strs[i].length <= 100
strs[i] is made up of lowercase English letters.
'''
from typing import List

class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    result = {}
    for s in strs: # s - string ex: "act"
      chars = [0]*26 #list of 26 [0]'s
      for el in s: 
        chars[ord(el)-ord('a')] += 1 #letter index/list
      chars = tuple(chars) # map key can only be immutable
      if result.get(chars): 
        result[chars].append(s) #append the string to the same key
      else:
        result[chars] = [s] # else new list
    '''
    time complexity (n * m) 
    n length of list
    m avg length of string in list
    '''
    return result.values()


solution = Solution()
print(solution.groupAnagrams(["act","pots","tops","cat","stop","hat"]))  # Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
print(solution.groupAnagrams(["x"]))    # Output: [["x"]]
print(solution.groupAnagrams([""]))       # Output: [[""]]
