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

        for n in nums: ## remember this iterates over nums length 
            if n in hashset:
                return True
            hashset.add(n)
        return False
    
solution2 = Solution2()
print(solution2.containsDuplicate(nums))


##** Possibly easiest solution syntax wise would be below
##** Sets do not contain duplicates therefore if the length of the set differs from the length of the array then we can
##** assume a duplicate present in array

class Solution3:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
    
solution3 = Solution3()
print(solution3.containsDuplicate(nums))






# nums2 = [1,1,1,3,3,4,3,2,4,2] ## True
# nums2 = [1,2,3,4,2,22,3,4,5,9] # False
nums2 = [1,2,3,4,2]

class Repition:
    def containsDuplicate(self, nums2: List[int]) -> bool:
        seen = set()

        for num in nums2:
            if num in seen:
                return True
            seen.add(num)
            print(seen)
        return False

    

repitiion = Repition()
print(repitiion.containsDuplicate(nums2))