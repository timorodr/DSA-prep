# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: 9 exists in nums and its index is 4
# Example 2:

# Input: nums = [-1,0,3,5,9,12], target = 2
# Output: -1
# Explanation: 2 does not exist in nums so return -1
 

# Constraints:

# 1 <= nums.length <= 104
# -104 < nums[i], target < 104
# All the integers in nums are unique.
# nums is sorted in ascending order.


from typing import List

nums = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]
target = 9


#** Essentially Binary search halves the available ascending order list and identifies which half of the list the target is in
#** and searches/havles that portion , repeating the process until the target is found/ or to see if it is in the list

#** We start with a sorted list
#** we identify left pointer to be at 0 and right pointer to be at the last index of list
#** We want to execute a while to run as long as left is less than or equal to right and
#** create a variable 'm' to identify the middle of our search (left + right) // 2
#** lastly we check with conditionals if our nums[m] value is greater than or less than the target and 
#** adjust the left and right pointers based on whats true. Ex: (if target is 9 and out middle point is 50 we want to move our right
#** pointer to m - 1 because we know 'm' is not the value and we only want to search the lesser half. And visa versa with the target
#** being greater than m. We would shift our left point to left = middle + 1 to search the greater half
#** if target not in list return out with -1

class Solution:
    def find_target(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 # initialize variables at 0-index and last-index

        while l <= r: # loop through array until l = r
            m = (l + r) // 2 # initialize variable to find middle of list
            if nums[m] > target: #compare middle value of list to target and move pointers either to right or left half based on if less than or greater than target
                print(m)
                r = m - 1
            elif nums[m] < target:
                print(m)
                l = m + 1
            else:
                return m
        return -1
    
solution = Solution()
print(solution.find_target(nums, target))