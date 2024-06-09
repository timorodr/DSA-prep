def isPrime(n):
    if n <= 1:
        return False
    # adding one to for loop to be inclusive of square root
    for i in range(2, int(n**0.5) + 1):
        print(i)
        if n % i == 0:
            return False
    return True

print(11**0.5)
# Example usage
# print(isPrime(11))  # True
print(isPrime(37))  # False

#** If we have range(2, int(n**0.5)), it generates numbers from 2 up to but not including the square root of n. So, for 
#** n=25, the square root is 5. range(2, 5) would generate [2, 3, 4], missing out on checking 5.
#
#** In Python, the range function includes the start number but excludes the end number. So, if we want to include the square root in our checks, we need to add 1.
