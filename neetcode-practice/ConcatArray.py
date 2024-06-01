# Given an integer array nums of length n, you want to create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

# Specifically, ans is the concatenation of two nums arrays.

# Return the array ans.

 

# Example 1:

# Input: nums = [1,2,1]
# Output: [1,2,1,1,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[0],nums[1],nums[2]]
# - ans = [1,2,1,1,2,1]
# Example 2:

# Input: nums = [1,3,2,1]
# Output: [1,3,2,1,1,3,2,1]
# Explanation: The array ans is formed as follows:
# - ans = [nums[0],nums[1],nums[2],nums[3],nums[0],nums[1],nums[2],nums[3]]
# - ans = [1,3,2,1,1,3,2,1]
 

# Constraints:

# n == nums.length
# 1 <= n <= 1000
# 1 <= nums[i] <= 1000
from typing import List

nums = [1,2,1]

##** We need to make sure we initialize a new array as the question calls for
##** We need to loop over each num in nums and append those nums to our ans array
##** We "for i in range(2)" essentially makes our nested for loop modular and available to run however many times we need within range parameter

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]: # without class we take out "self" argument in def
        ans = []
        for i in range(2):
            for num in nums:
                ans.append(num)
        return ans

solution = Solution()
print(solution.getConcatenation(nums))
