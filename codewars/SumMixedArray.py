# Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

# Return your answer as a number.



arr = [5, '4', 3, 4, '9']

def sum_mix(arr):
    return sum(int(i) for i in arr)

solution = sum_mix(arr)
print(type(solution))
print(solution)