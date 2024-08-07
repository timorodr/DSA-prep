# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.

# After doing so, return the array.

 

# Example 1:

# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
# Explanation: 
# - index 0 --> the greatest element to the right of index 0 is index 1 (18).
# - index 1 --> the greatest element to the right of index 1 is index 4 (6).
# - index 2 --> the greatest element to the right of index 2 is index 4 (6).
# - index 3 --> the greatest element to the right of index 3 is index 4 (6).
# - index 4 --> the greatest element to the right of index 4 is index 5 (1).
# - index 5 --> there are no elements to the right of index 5, so we put -1.
# Example 2:

# Input: arr = [400]
# Output: [-1]
# Explanation: There are no elements to the right of index 0.
 

# Constraints:

# 1 <= arr.length <= 104
# 1 <= arr[i] <= 105

from typing import List

arr = [17,18,5,4,6,1]

class Solution:
    def find_target(self, arr: List[int]) -> List[int]:
        rightMax = -1

        for i in range(len(arr) -1, -1, -1):
            newMax = max(rightMax, arr[i])
            arr[i] = rightMax
            rightMax = newMax
        return arr


    
solution = Solution()
print(solution.find_target(arr))




arr = [17,18,5,4,6,1]

rightMax = -1

for i in range(len(arr) -1, -1, -1):
    newMax = max(rightMax, arr[i]) # either 1 or -1 // either 1 or 6 // either 6 or 4
    arr[i] = rightMax # last index initially is -1 // arr[i] is now 6 // keep 6 
    rightMax = newMax # right max is now 1 // right max 6 // still 6 so one and so forth
return arr