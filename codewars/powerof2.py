# Complete the function that takes a non-negative integer n as input, and returns a list of all the powers of 2 with the exponent ranging from 0 to n ( inclusive ).




def powers_of_two(n):
    ans = []
    
    for i in range(n + 1):
        result = 2**i
        ans.append(result)
    print(ans)

powers_of_two(5)