# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

# Constraints:

# -231 <= x <= 231 - 1

#* Pretty simple, just have to convert int to str to reverse the string and compare. less than 0 will always be false as (-) negative will never be in correct position

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        elif str(x)[::-1] == str(x):
            return True
        

# Follow up: check if palindrom number without converting to string. In this instance, we would 
# have to (in a round about way) mod every number and divide every number for however large the number is 
# to check the placing of each digit 