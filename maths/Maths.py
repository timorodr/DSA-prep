
# for i in range(len(nums)):
#     print(nums[i])

# for n in nums:
#     print(n)

# for i, n in enumerate(nums):
#     print(i, n)

##* sorts and reverses [2,1,1]
# nums.sort(reverse=True)
# print(nums)

# arr = ["bob", "alice", "jane", "doe"]
# arr.sort()
# print(arr)

##** custom sort by length of string
#* OUTPUT ['bob', 'doe', 'jane', 'alice']
# arr.sort(key=lambda x: len(x))
# print(arr)

##* builds list 0 through 4
# arr = [i for i in range(5)]
# print(arr)

##** 2-D lists
# arr = [[0] * 4 for i in range(4)]
# print(arr)
# print(arr[0][0], arr[3][3])

# class MyClass:
#     # Constructor
#     def __init__(self, nums):
#         # Create member variables
#         self.nums = nums
#         self.size = len(nums)
    
#     # self key word required as param
#     def getLength(self):
#         return self.size

#     def getDoubleLength(self):
#         return 2 * self.getLength()

# myObj = MyClass([1, 2, 3])
# print(myObj.getLength())
# print(myObj.getDoubleLength())

# def outer(a, b):
#     c = "c"

#     def inner():
#         return a + b + c
#     return inner()

# print(outer("x", "b"))

# nums1 = [1, 3, 5]
# nums2 = [2, 4, 6]
# for n1, n2 in zip(nums1, nums2):
#     print(n1, n2)

# arr = [5, 4, 7, 3, 8]
# arr.sort()
# print(arr)

# a, b, c = [1, 2, 3]
# print(a, b, c)

# for i in range(5):
#     print("1st",i)

# for i in range(2,6):
#     print("2nd", i)

# for i in range(5, 1, -1):
#     print("3rd",i)

# print(int(-3/2))

# import math
# from multiprocessing import heap
# print(math.fmod(-10, 3)) # 1

# ## BE CAREFUL with negative modulo DO THE ABOVE
# print(10 % 3) # 1
# print(-10 % 3) # 2

# nums.insert(1, 7)
# print(nums)

# n = 5
# arr = [1] * n
# print(arr)
# print(len(arr))
# # [1,1,1,1,1]

# arr2 = [1, 2, 3, 4]
# print(arr2[1:3])
# #[2,3]
    

prevMap = {4:0, 1:1, 9:2, 7:3}

print(prevMap[9])