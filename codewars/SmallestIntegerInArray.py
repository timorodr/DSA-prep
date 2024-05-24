# Given an array of integers your solution should find the smallest integer.

# For example:

# Given [34, 15, 88, 2] your solution will return 2
# Given [34, -345, -1, 100] your solution will return -345
# You can assume, for the purpose of this kata, that the supplied array will not be empty.

arr = [34, 15, 88, 2]

def findSmallestInt(arr):
    return min(arr)

print(findSmallestInt(arr))

##** OR

def findSmallestInt2(arr):
    arr.sort()
    return arr[0]

print(findSmallestInt2(arr))
