# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "()[]{}"
# Output: true
# Example 3:

# Input: s = "(]"
# Output: false
 

# Constraints:

# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

#* Create a stack with open paranthesis and popping if a match 
#* appending to stack if an open paranthesis

# class Solution:
#     def isValid(self, s: str) -> bool:
#         stack = []
#         lookup = {")": "(", "]": "[", "}": "{"}

#         for c in s:
#             if c in lookup:
#                 if stack and stack[-1] == lookup[c]:
#                     stack.pop()
#                 else:
#                     return False
#             else:
#                 stack.append(c)

#         return stack == []
    

s = "()[]{}"

class Solution:
    
    

solution = Solution()
print(solution.isValid(s))
