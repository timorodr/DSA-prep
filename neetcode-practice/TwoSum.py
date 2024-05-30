# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

 

# Example 1:

# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
# Example 2:

# Input: nums = [3,2,4], target = 6
# Output: [1,2]
# Example 3:

# Input: nums = [3,3], target = 6
# Output: [0,1]
 

# Constraints:

# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.





from typing import List

##** THIS IS THE BRUTE FORCE APPROACH USING 2 POINTERS TO LOOP OVER ARRAY 
##** AND KEEPING TRACK OF L WHILE R LOOPS THROUGH REMAINDER OF ARRAY LOOKING FOR MATCHING INT TO ADD UP TO TARGET VALUE
##** THIS IS O(n^2)

nums = [2,1,7,11,15]
target = 9

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for L in range(len(nums)):
            for R in range(L + 1, len(nums)): ## L + 1 always points to the element to the Right of L
                if nums[L] + nums[R] == target:
                    return [L, R]
        return
    

solution = Solution()
print(solution.twoSum(nums, target))


##** This is the optimal solution here utilizing a hashmap of previously seen numbers with their index (questions answer calls for indices)
##** to obtain num and index we neep to use for i, n in enumerate(nums): python loop
##** We know that there is exactly one solution.

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # create the hashmap

        for i, n in enumerate(nums):
            diff = target - n ## this way we are able to eventually see if the diff is in the hashmap already
            if diff in seen: ## if the difference is in our HM
                return [seen[diff], i]
            seen[n] = i ## if the current (num) key is not in HM we want to add it in and assign its value as i
        return 

solution2 = Solution2()
print(solution2.twoSum(nums, target))

