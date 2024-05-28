# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

##** first idea is brute force to loop through every value in array and compare to a specific value using another loop
##** returning True if duplicate and False if not matched to specified value
##** it would look like this. Good to know but this is slow


from typing import List


# nums = [1,2,3,1] ## True
# nums = [1,2,3,4] ## False
nums = [1,1,1,3,3,4,3,2,4,2] ## True

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
    
solution = Solution()
print(solution.containsDuplicate(nums))


##** the 2nd and better approach is to create a hashmap with all of the seen values and comparing value of array to those seen in hashmap
##** would look like so:

class Solution2:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
    
solution2 = Solution2()
print(solution2.containsDuplicate(nums))