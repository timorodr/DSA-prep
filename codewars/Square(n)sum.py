# Complete the square sum function so that it squares each number passed into it and then sums the results together.

# For example, for [1, 2, 2] it should return 9 because 
# 1
# 2
# +
# 2
# 2
# +
# 2
# 2
# =
# 9
# 1 
# 2
#  +2 
# 2
#  +2 
# 2
#  =9.


numbers = [1,2,2]

def square_sum(numbers):
    ans = []
    
    for n in numbers:
        square = n * n
        ans.append(square)
    return sum(ans)

print(square_sum(numbers))


# ** OR

def square_sum(numbers):
    return sum(x ** 2 for x in numbers)