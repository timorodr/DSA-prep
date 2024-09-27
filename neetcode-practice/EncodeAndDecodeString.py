
# String Encode and Decode
# Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

# Please implement encode and decode

# Example 1:

# Input: ["neet","code","love","you"]

# Output:["neet","code","love","you"]
# Example 2:

# Input: ["we","say",":","yes"]

# Output: ["we","say",":","yes"]
# Constraints:

# 0 <= strs.length < 100
# 0 <= strs[i].length < 200
# strs[i] contains only UTF-8 characters.

from typing import List

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for c in strs:
            length = str(len(c))
            res += length + "#" + c
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
                length = int(s[i:j])
                res.append(s[j + 1: j + length + 1])
                i = j + length + 1
        return res
    
##* very important to remember that we properly use python splice to grab values we want then update position of i





class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for word in strs:
            res += str(len(word)) + "#" + word
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while j != "#":
                j += 1
                length = int(s[i:j])
                res.append(s[j + 1: j + 1 + length])
                i = j + 1 + length
        return res
    
# remember to use 2 pointers to solve. J to find # and i to get the length of the word to append
