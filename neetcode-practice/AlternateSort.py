
from typing import List

nums = [1,2,3,4,5,6,7,8]

class Solution:
    def altSort(self, nums: List[str]) -> int:
        
        for i in range(0, len(nums), 2): #alt sort just remembering that 1st arg is starting place, 2nd arg is ending, and 3rd arg is increment value
            print(nums[i])

solution = Solution()
print(solution.altSort(nums))