# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

# Example 1:

haystack = "sadbutsad"

needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

# Constraints:

# 1 <= haystack.length, needle.length <= 104
# haystack and needle consist of only lowercase English characters.

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) + 1 - len(needle)): # loop through the length of the haystack string until we know that the remaining characters are still long enough to equal the length of needle
            if haystack[i: i + len(needle)] == needle: # slices a substring in haystack starting at i until the length of needle +1 bc not inclusive is equal to the string needle
                return i #return the index we started on to complete the sequence and check for substring
        return -1
    
# loop through then conditional  haystack slice if it is equal to slice