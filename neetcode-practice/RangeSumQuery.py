from typing import List


nums = [-2, 0, 3, -5, 2, -1]

class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix = []
        cur = 0
        for n in nums:
            self.prefix.append(n)
        print(self.prefix)

    def sumRange(self, left: int, right: int) -> int:
        
    
obj = NumArray(nums)
param_1 = obj.sumRange(0,2)
print(param_1)