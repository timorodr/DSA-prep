
from typing import List

nums = [1,2,3,4,5,6,7,8]

class Solution:
    def altSort(self, nums: List[str]) -> int:

        # res = []

        # for i in range(0, len(nums), 2):
        #     res.append(nums[i])
        
        return nums[::2]

solution = Solution()
print(solution.altSort(nums))