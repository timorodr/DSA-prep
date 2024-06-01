# Your task is to find the nearest square number, nearest_sq(n) or nearestSq(n), of a positive integer n.

# For example, if n = 111, then nearest\_sq(n) (nearestSq(n)) equals 121, since 111 is closer to 121, the square of 11, than 100, the square of 10.

# If the n is already the perfect square (e.g. n = 144, n = 81, etc.), you need to just return n.

import math

def nearest_sq(n):
    squared = math.sqrt(n)
    ans = (round(squared)) * (round(squared))
    return ans

print(nearest_sq(111))


# POP API
# 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 
