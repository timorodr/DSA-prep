# Write a function which calculates the average of the numbers in a given list.

# Note: Empty arrays should return 0.

numbers = [1,4,55,5,6,77,8,8,66,54,3]

def find_average(numbers):
    count = 0

    if numbers == []:
        return 0

    for num in numbers:
        count += num
    return count/len(numbers)
#   return sum(numbers)/len(numbers)

print(find_average(numbers))