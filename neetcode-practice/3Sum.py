# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.

from typing import List

nums = [-4, -2, -1, -1, 0, 1, 2]
target = 0

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        res = []
        nums.sort()

        for i, num in enumerate(nums): # loop through index and value checking if 1-index is true and if its the same as previous then continue
            if i > 0 and num == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) - 1 # create variables for 1-index and last index
            while l < r: # loop as long as l<r and create a 3sum variable that is the values of all 3 added together
                threeSum = num + nums[l] + nums[r]
                if threeSum > 0: # based on 3sum value we decrement or increment bc the nums are sorted
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([num, nums[l], nums[r]]) # if 3sum = 0 then we append to our res and move l to the next index
                    l += 1
                    while l < r and nums[l] == nums[l - 1]: # we loop and make sure that l isnt same as previous value we just used - if it is then we move l 1-index until it is unique value
                        l += 1
        return res