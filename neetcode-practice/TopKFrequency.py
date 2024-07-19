# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

 

# Example 1:

# Output: [1,2]
# Example 2:

# Input: nums = [1], k = 1
# Output: [1]
 

# Constraints:

# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
 

# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
nums = [1,1,1,2,2,3]
k = 2

from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        top_seen = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            top_seen[num] = top_seen.get(num, 0) + 1
        
        for number, count in top_seen.items():
            freq[count].append(number)
        
        res = []

        for i in range(len(freq) -1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
        
solution = Solution()
print(solution.topKFrequent(nums, k))

## revisit after ec2 deployment
## nginx and gunicorn active but 502 bad gateway error present
## DSA revamp with streaming 

## create a hashmap of each num in nums and set its frequency to the key of that num.
## create a freq array USING BUCKET SORT [[], [], [], [], []] 
## basically the frequency list is a list where each value is also a list.
## we need to append the number in nums to the frequency it appears as the index in our freq list so...
## [1,1,1,2,2,3] = [[], [3], [2], [1], [], [], [], []] 
## 3 appears 1 time so we append the number 3 to the index 1 etc.,
## loop through the freq backwards then loop through the list at that index and append the value to our res = []
## when our res list == the length of k we return the res list